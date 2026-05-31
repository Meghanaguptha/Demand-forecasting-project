import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import joblib
import numpy as np

def train_model(df):
    """
    Trains a Multiple Regression model and a Random Forest model.
    """
    # 1. Feature Selection
    features = ['Store', 'DayOfWeek', 'Promo', 'StateHoliday', 'StoreType', 'Assortment', 
                'CompetitionDistance', 'Year', 'Month', 'Day', 'WeekOfYear']
    X = df[features]
    y = df['Sales']
    
    # 2. Split Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Multiple Linear Regression
    print("Training Multiple Linear Regression...")
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    
    # 4. Random Forest (For better accuracy, as a 'Unique Angle')
    print("Training Random Forest Regressor (this may take a minute)...")
    rf_model = RandomForestRegressor(n_estimators=50, max_depth=15, n_jobs=-1, random_state=42)
    rf_model.fit(X_train, y_train)
    
    # 5. Evaluation
    def evaluate(model, name):
        preds = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, preds))
        mae = mean_absolute_error(y_test, preds)
        print(f"--- {name} Metrics ---")
        print(f"RMSE: {rmse:.2f}")
        print(f"MAE:  {mae:.2f}")
        return rmse, mae

    evaluate(lr_model, "Linear Regression")
    evaluate(rf_model, "Random Forest")
    
    # 6. Save Models
    joblib.dump(lr_model, 'src/lr_model.joblib')
    joblib.dump(rf_model, 'src/rf_model.joblib')
    joblib.dump(features, 'src/features_list.joblib')
    print("Models and features list saved to src/ folder.")

if __name__ == "__main__":
    from data_loader import load_data
    from preprocessing import preprocess_data
    try:
        raw_data = load_data()
        clean_data = preprocess_data(raw_data)
        train_model(clean_data)
    except Exception as e:
        print(f"Error during modeling: {e}")
