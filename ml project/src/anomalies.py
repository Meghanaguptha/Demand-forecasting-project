import pandas as pd
import numpy as np

def detect_anomalies(df):
    """
    Identifies sales anomalies using Z-score methodology.
    """
    # Calculate mean and std for each store to find store-specific anomalies
    df['Sales_Mean'] = df.groupby('Store')['Sales'].transform('mean')
    df['Sales_Std'] = df.groupby('Store')['Sales'].transform('std')
    
    # Calculate Z-score
    df['Z_Score'] = (df['Sales'] - df['Sales_Mean']) / df['Sales_Std']
    
    # Define anomalies as Z-score > 3 (spikes) or < -3 (plummets)
    anomalies = df[np.abs(df['Z_Score']) > 3].copy()
    
    # Sort by significance
    anomalies = anomalies.sort_values(by='Z_Score', ascending=False)
    
    print(f"Detected {len(anomalies)} anomalies in the dataset.")
    return anomalies

def get_anomaly_summary(anomaly_row):
    """
    Format a single anomaly into a string for Claude to explain.
    """
    summary = f"""
    Store: {anomaly_row['Store']}
    Date: {anomaly_row['Date']}
    Actual Sales: ${anomaly_row['Sales']:,.2f}
    Expected Mean: ${anomaly_row['Sales_Mean']:,.2f}
    Z-Score: {anomaly_row['Z_Score']:.2f}
    Promotion Active: {anomaly_row['Promo']}
    State Holiday: {anomaly_row['StateHoliday']}
    """
    return summary
