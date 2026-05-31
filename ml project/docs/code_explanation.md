# Code Explanation

This document explains each code component in the Retail Demand Forecasting project.

## `app.py`
- Builds the Streamlit dashboard for interactive demand simulation.
- Loads pretrained models (`lr_model.joblib`, `rf_model.joblib`) from `src/`.
- Provides a control panel for store ID, promotion status, day of week, and state holiday.
- Displays forecast predictions from Linear Regression and Random Forest.
- Uses `GenAIEngine` to provide narrative insights and anomaly explanations.
- Contains a fallback warning when models are not available.

## `run_pipeline.py`
- Orchestrates the end-to-end workflow.
- Loads raw data via `src.data_loader.load_data()`.
- Cleans data using `src.preprocessing.preprocess_data()`.
- Generates EDA visuals with `src.eda.run_eda()`.
- Trains models using `src.model.train_model()`.
- Prints status updates and saves artifacts to the workspace.

## `src/data_loader.py`
- Reads `data/train.csv` and `data/store.csv`.
- Converts the `Date` column to datetime.
- Merges store metadata into the transaction dataset.
- Ensures the dataset is ready for preprocessing and model training.

## `src/preprocessing.py`
- Handles missing values for competition and promo-related fields.
- Extracts date features: year, month, day, and week of year.
- Normalizes `StateHoliday` labels and filters to open store days.
- Encodes categorical columns into numeric values for modeling.

## `src/eda.py`
- Generates visualizations for sales distribution and seasonal patterns.
- Creates a boxplot to compare sales by promotion status.
- Produces a correlation heatmap for key numeric features.
- Saves charts into the `notebooks/` folder so they can be reused in reports.

## `src/model.py`
- Trains two regression models:
  - `LinearRegression`
  - `RandomForestRegressor`
- Splits data into training and test sets.
- Computes RMSE and MAE evaluation metrics.
- Saves model objects and feature metadata for the dashboard.

## `src/anomalies.py`
- Detects anomalies using a Z-score method per store.
- Calculates store-level mean and standard deviation.
- Selects extreme sales records with absolute Z-scores above 3.
- Formats anomaly details into a summary for AI explanation.

## `src/genai_engine.py`
- Wraps Anthropic Claude API calls for narrative insights.
- Supports three functions:
  - `get_demand_insights()` for strategic recommendations
  - `chat_with_analyst()` for natural language questions
  - `explain_anomaly()` for anomaly interpretation
- Reads `ANTHROPIC_API_KEY` from `.env`.

## `Dockerfile`
- Defines a container image using Python 3.11.
- Installs dependencies from `requirements.txt`.
- Sets `app.py` as the Streamlit app entrypoint.
- Exposes port 8501 for browser access.

## `Procfile`
- Defines the Streamlit process for cloud hosting platforms.
- Ensures the app starts on the designated platform port.

## `requirements.txt`
- Lists project dependencies required for model training, visualization, and serving.
- Includes `python-pptx` for generating the presentation.

## `.env`
- Stores the Anthropic API key.
- Example entry:
  - `ANTHROPIC_API_KEY=your_api_key_here`

## Notes
- `src` contains the core ML and AI logic.
- `docs/` contains the project report, code explanation, and deployment guide.
- `notebooks/` stores generated EDA images and assets for the presentation.
