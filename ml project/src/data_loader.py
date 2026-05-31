import pandas as pd
import os

def load_data(data_dir='data'):
    """
    Loads train and store datasets and merges them.
    """
    train_path = os.path.join(data_dir, 'train.csv')
    store_path = os.path.join(data_dir, 'store.csv')
    
    if not os.path.exists(train_path) or not os.path.exists(store_path):
        raise FileNotFoundError(f"Dataset files not found in {data_dir}. Please download them from Kaggle.")
    
    # Load with low_memory=False to avoid DtypeWarning
    train = pd.read_csv(train_path, low_memory=False)
    store = pd.read_csv(store_path)
    
    # Pre-merging: Convert Date to datetime
    train['Date'] = pd.to_datetime(train['Date'])
    
    # Merge datasets
    df = pd.merge(train, store, on='Store', how='left')
    
    print(f"Data loaded successfully. Shape: {df.shape}")
    return df

if __name__ == "__main__":
    # Example usage
    try:
        data = load_data()
        print(data.head())
    except FileNotFoundError as e:
        print(e)
