from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.eda import run_eda
from src.model import train_model
import os

def main():
    print("=== Starting 30% Submission Workflow ===")
    
    # Check if data exists
    if not os.path.exists('data/train.csv'):
        print("ALERT: data/train.csv not found.")
        print("Please download 'rossmann-store-sales' from Kaggle and place CSVs in 'data/' folder.")
        return

    # Step 0: Ensure output folders exist
    os.makedirs('notebooks', exist_ok=True)

    # Step 1: Load
    df = load_data()
    
    # Step 2: Preprocess
    df_clean = preprocess_data(df)
    
    # Step 3: EDA
    run_eda(df_clean)
    
    # Step 4: Model
    train_model(df_clean)
    
    print("\n=== Workflow Completed Successfully ===")
    print("You can now find visualizations in the 'notebooks/' folder and models in 'src/'.")

if __name__ == "__main__":
    main()
