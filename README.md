# Demand-forecasting-project
# 🛒 Retail Demand Forecasting using Machine Learning and Generative AI

## 📌 Project Overview

Retail businesses often face challenges in maintaining optimal inventory levels due to fluctuating customer demand. Overestimating demand leads to excess inventory costs, while underestimating demand results in stock shortages and lost sales.

This project presents an end-to-end **Retail Demand Forecasting System** built using the **Rossmann Store Sales Dataset**. The system leverages Machine Learning techniques to predict future sales demand and integrates Generative AI to generate intelligent business insights from forecasted results.

The solution includes data preprocessing, exploratory data analysis (EDA), model training, anomaly detection, demand prediction, AI-powered insights generation, and an interactive Streamlit dashboard for visualization.

---

## 🎯 Objectives

* Analyze historical retail sales data.
* Identify factors influencing product demand.
* Build predictive machine learning models for demand forecasting.
* Generate business-friendly demand insights using Generative AI.
* Visualize predictions and trends through an interactive dashboard.
* Provide a deployment-ready solution using Docker.

---

## 🛠️ Technologies Used

### Programming Language

* Python 3.9+

### Machine Learning & Data Analysis

* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Matplotlib
* Seaborn

### Web Application

* Streamlit

### Generative AI

* Anthropic Claude API

### Deployment

* Docker
* Procfile

---

## 📂 Project Structure

```text
Retail-Demand-Forecasting/
│
├── app.py                        # Streamlit dashboard
├── run_pipeline.py               # Data processing & model training
├── generate_presentation.py      # Auto-generates project presentation
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Docker configuration
├── Procfile                      # Deployment configuration
│
├── data/
│   ├── train.csv
│   ├── store.csv
│   └── test.csv
│
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── anomaly_detection.py
│   ├── genai_insights.py
│   └── utils.py
│
├── docs/
│   ├── Project_Report.pdf
│   ├── Deployment_Guide.pdf
│   └── Code_Explanation.pdf
│
└── outputs/
    ├── trained_models/
    ├── visualizations/
    └── forecasts/
```

---

## 📊 Dataset

This project uses the **Rossmann Store Sales Dataset**, which contains historical sales information from Rossmann stores.

Dataset includes:

* Store Information
* Daily Sales
* Promotions
* Holidays
* Customer Trends
* Store Characteristics

📥 Download Dataset:
https://www.kaggle.com/competitions/rossmann-store-sales

After downloading, place the following files inside the `data/` folder:

```text
data/
├── train.csv
├── store.csv
└── test.csv
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/retail-demand-forecasting.git

cd retail-demand-forecasting
```

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## 🔑 Environment Configuration

Create a `.env` file in the project root directory:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

This API key is required for AI-generated business insights.

---

## 🚀 Running the Project

### Step 1: Train the Models

Run the complete data pipeline:

```bash
python run_pipeline.py
```

This process performs:

* Data Loading
* Data Cleaning
* Feature Engineering
* Exploratory Data Analysis
* Model Training
* Performance Evaluation
* Forecast Generation

---

### Step 2: Launch the Dashboard

```bash
streamlit run app.py
```

The dashboard provides:

* Sales Trend Visualization
* Demand Forecasting
* Business Insights
* Forecast Simulation
* AI-Generated Recommendations

---

### Step 3: Generate Project Presentation

```bash
python generate_presentation.py
```

This automatically creates a PowerPoint presentation containing:

* Problem Statement
* Methodology
* EDA Results
* Model Performance
* Forecast Analysis
* Conclusion

---

## 🤖 Machine Learning Workflow

```text
Raw Data
    │
    ▼
Data Preprocessing
    │
    ▼
Feature Engineering
    │
    ▼
Exploratory Data Analysis
    │
    ▼
Model Training
    │
    ▼
Demand Prediction
    │
    ▼
Anomaly Detection
    │
    ▼
Generative AI Insights
    │
    ▼
Dashboard Visualization
```

---

## 📈 Key Features

✅ Retail Sales Forecasting

✅ Data Cleaning & Feature Engineering

✅ Exploratory Data Analysis (EDA)

✅ Multiple Machine Learning Models

✅ Forecast Accuracy Evaluation

✅ Anomaly Detection

✅ Interactive Streamlit Dashboard

✅ Generative AI Business Insights

✅ Docker Deployment Support

✅ Automated Presentation Generation

---

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t retail-demand-forecasting .
```

### Run Docker Container

```bash
docker run -p 8501:8501 --env-file .env retail-demand-forecasting
```

Access the application at:

```text
http://localhost:8501
```

---

## 📊 Expected Output

The system generates:

* Sales Forecasts
* Demand Trend Analysis
* Forecast Accuracy Metrics
* AI-Powered Business Recommendations
* Interactive Data Visualizations

---

## 📚 Future Enhancements

* Real-time demand forecasting
* Cloud deployment (AWS/Azure/GCP)
* Deep Learning Models (LSTM, GRU)
* Multi-store inventory optimization
* Automated retraining pipeline
* Advanced GenAI reporting

---

## 👨‍💻 Contributors

* Meghana Eruvanti
  

---

## 📄 License

This project is developed for academic and educational purposes.

---

## 🙏 Acknowledgements

* Rossmann Store Sales Dataset
* Kaggle
* Scikit-learn Community
* Streamlit
* Anthropic Claude API
* Open Source Python Ecosystem

