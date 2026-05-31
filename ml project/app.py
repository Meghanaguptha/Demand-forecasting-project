import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go
from src.genai_engine import GenAIEngine
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Demand AI Analyst", page_icon="📈", layout="wide")

# --- LOAD ASSETS ---
@st.cache_resource
def load_models():
    lr_model = joblib.load('src/lr_model.joblib')
    rf_model = joblib.load('src/rf_model.joblib')
    features = joblib.load('src/features_list.joblib')
    return lr_model, rf_model, features

# Fallback for when models aren't trained yet
models_exist = os.path.exists('src/rf_model.joblib') and os.path.exists('src/lr_model.joblib') and os.path.exists('src/features_list.joblib')
if models_exist:
    lr_model, rf_model, features = load_models()
else:
    st.warning("Models not found. Please run the training pipeline first by executing `python run_pipeline.py`.")

genai = GenAIEngine()

# --- CUSTOM CSS ---
st.markdown("""
<style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    .stSidebar { background-color: #161b22; }
</style>
""", unsafe_allow_html=True)

if not genai.client:
    st.sidebar.warning("GenAI is disabled because the Anthropic API key is missing or invalid. Update .env with a valid key.")

# --- SIDEBAR ---
st.sidebar.title("🛠️ Demand Controls")
st.sidebar.info("Adjust inputs to see real-time demand changes.")

store_id = st.sidebar.number_input("Store ID", min_value=1, max_value=1115, value=1)
promo = st.sidebar.toggle("Active Promotion (Promo)", value=True)
day_of_week = st.sidebar.slider("Day of Week (1=Mon, 7=Sun)", 1, 7, 1)
holiday = st.sidebar.selectbox("State Holiday", ["None", "Public", "Easter", "Christmas"])
holiday_map = {"None": 0, "Public": 1, "Easter": 2, "Christmas": 3}

# --- HEADER ---
st.title("📊 Demand Forecasting in Retail")
st.markdown("### Multiple Regression + GenAI Insights")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🔮 What-If Demand Simulator")
    
    # Simulation Data Preparation
    # ['Store', 'DayOfWeek', 'Promo', 'StateHoliday', 'StoreType', 'Assortment', 'CompetitionDistance', 'Year', 'Month', 'Day', 'WeekOfYear']
    # Hardcoded/Default values for some fields for simulation
    sim_data = {
        'Store': store_id,
        'DayOfWeek': day_of_week,
        'Promo': 1 if promo else 0,
        'StateHoliday': holiday_map[holiday],
        'StoreType': 3, # Default Type 'c'
        'Assortment': 1, # Default Assortment 'a'
        'CompetitionDistance': 1200,
        'Year': 2026,
        'Month': 12,
        'Day': 15,
        'WeekOfYear': 51
    }
    
    if models_exist:
        sim_df = pd.DataFrame([sim_data])
        lr_pred = lr_model.predict(sim_df[features])[0]
        rf_pred = rf_model.predict(sim_df[features])[0]
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Linear Regression Prediction", f"${lr_pred:,.2f}")
        c2.metric("Random Forest Prediction", f"${rf_pred:,.2f}", delta=f"{((rf_pred-lr_pred)/lr_pred)*100:.1f}%")
        c3.metric("Status", "High Demand" if rf_pred > 8000 else "Stable")

        # Visualizing Simulation
        st.write("---")
        st.write("**Impact of Inputs on Demand**")
        
        # Simple comparison chart
        fig = go.Figure(data=[
            go.Bar(name='Linear Regression', x=['Forecast'], y=[lr_pred], marker_color='#1f77b4'),
            go.Bar(name='Random Forest', x=['Forecast'], y=[rf_pred], marker_color='#00cc96')
        ])
        fig.update_layout(barmode='group', template="plotly_dark", height=300)
        st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("🤖 AI Chat Analyst")
    st.write("Ask Claude about the forecast results.")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Ex: Why is demand higher with a promo?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            context = f"Forecast values: LR=${lr_pred:.0f}, RF=${rf_pred:.0f}. Promo={promo}, Holiday={holiday}."
            response = genai.chat_with_analyst(prompt, context)
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# --- BOTTOM SECTION: DATA INSIGHTS ---
st.write("---")
tab1, tab2 = st.tabs(["💡 Strategic Insights", "🚨 Anomaly Detection"])

with tab1:
    if st.button("🪄 Generate Strategic AI Report"):
        with st.spinner("Claude is analyzing seasonal trends..."):
            summary = f"Simulation Summary: Store {store_id} is predicted to have sales of ${rf_pred:,.2f} on a {day_of_week} in December with Promo={promo}."
            insights = genai.get_demand_insights(summary)
            if "unavailable" in insights.lower() or "api error" in insights.lower():
                st.error(insights)
            else:
                st.success("AI Insights Generated!")
                st.markdown(insights)

with tab2:
    st.subheader("Detecting Unusual Demand Patterns")
    st.write("This section identifies historical anomalies and uses Claude to explain them.")
    
    # In a real app, we would load the dataset here. 
    # For simulation, we'll show how it would look with example data.
    if st.button("🔍 Scan for Anomalies"):
        example_anomaly = {
            'Store': store_id,
            'Date': '2025-12-24',
            'Sales': 25430.00,
            'Sales_Mean': 8500.00,
            'Z_Score': 4.2,
            'Promo': 1,
            'StateHoliday': 'Christmas'
        }
        
        st.warning(f"Extreme Spike Detected on {example_anomaly['Date']}!")
        col_m1, col_m2 = st.columns(2)
        col_m1.metric("Actual Sales", f"${example_anomaly['Sales']:,.2f}")
        col_m1.metric("Z-Score", f"{example_anomaly['Z_Score']:.1f}")
        
        with st.spinner("Claude is investigating the cause..."):
            from src.anomalies import get_anomaly_summary
            # Mocking the row object for formatting
            summary_info = get_anomaly_summary(example_anomaly)
            explanation = genai.explain_anomaly(summary_info)
            if "unavailable" in explanation.lower() or "api error" in explanation.lower():
                st.error(explanation)
            else:
                st.info("**AI Forensic Explanation:**")
                st.write(explanation)
