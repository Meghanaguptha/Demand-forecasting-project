import pandas as pd
import numpy as np

def preprocess_data(df):
    """
    Cleans and prepares the retail data for modeling.
    """
    # 1. Handle missing values in store-specific columns
    # Fill CompetitionDistance with a large number (meaning far away)
    df['CompetitionDistance'] = df['CompetitionDistance'].fillna(df['CompetitionDistance'].max() * 2)
    
    # Fill other competition/promo columns with 0
    cols_to_fill = ['CompetitionOpenSinceMonth', 'CompetitionOpenSinceYear', 
                    'Promo2SinceWeek', 'Promo2SinceYear', 'PromoInterval']
    for col in cols_to_fill:
        df[col] = df[col].fillna(0)
    
    # 2. Extract Date Features
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['WeekOfYear'] = df['Date'].dt.isocalendar().week.astype(int)
    
    # 3. Handle categorical variables
    # StateHoliday has mixed types (0, "0", "a", "b", "c")
    df['StateHoliday'] = df['StateHoliday'].astype(str).replace('0', 'None')
    
    # 4. Filter for Open stores and non-zero sales (common practice for this dataset)
    # Most teachers prefer predicting non-zero demand
    df = df[df['Open'] != 0]
    df = df[df['Sales'] > 0]
    
    # 5. Encoding
    # Map StoreType and Assortment to numbers
    mappings = {
        'StoreType': {'a': 1, 'b': 2, 'c': 3, 'd': 4},
        'Assortment': {'a': 1, 'b': 2, 'c': 3},
        'StateHoliday': {'None': 0, 'a': 1, 'b': 2, 'c': 3}
    }
    for col, mapping in mappings.items():
        df[col] = df[col].map(mapping)
        
    print(f"Preprocessing complete. Final shape: {df.shape}")
    return df

if __name__ == "__main__":
    from data_loader import load_data
    try:
        raw_data = load_data()
        clean_data = preprocess_data(raw_data)
        print(clean_data.head())
    except Exception as e:
        print(f"Error during preprocessing: {e}")
