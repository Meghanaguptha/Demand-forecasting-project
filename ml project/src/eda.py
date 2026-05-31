import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def run_eda(df):
    """
    Generates key visualizations for demand forecasting.
    """
    sns.set(style="whitegrid")
    
    # 1. Sales Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Sales'], bins=50, kde=True)
    plt.title('Distribution of Sales')
    plt.savefig('notebooks/sales_dist.png')
    plt.close()
    
    # 2. Sales vs Promo
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Promo', y='Sales', data=df)
    plt.title('Impact of Promotion on Sales')
    plt.savefig('notebooks/sales_vs_promo.png')
    plt.close()
    
    # 3. Seasonal Trends (Monthly)
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Month', y='Sales', data=df)
    plt.title('Average Sales by Month')
    plt.savefig('notebooks/sales_monthly.png')
    plt.close()
    
    # 4. Correlation Matrix
    plt.figure(figsize=(12, 10))
    corr = df[['Sales', 'Customers', 'CompetitionDistance', 'Promo', 'DayOfWeek', 'Month']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.savefig('notebooks/correlation_matrix.png')
    plt.close()
    
    print("EDA Visualizations saved to notebooks/ folder.")

if __name__ == "__main__":
    from data_loader import load_data
    from preprocessing import preprocess_data
    try:
        raw_data = load_data()
        clean_data = preprocess_data(raw_data)
        run_eda(clean_data)
    except Exception as e:
        print(f"Error during EDA: {e}")
