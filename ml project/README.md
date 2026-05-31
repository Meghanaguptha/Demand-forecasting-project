# Retail Demand Forecasting Project

This repository delivers a complete retail demand forecasting solution using the Rossmann Store Sales dataset. It includes data ingestion, preprocessing, exploratory data analysis, model training, a Streamlit dashboard, GenAI insights, and deployment-ready artifacts.

## What is included
- `run_pipeline.py`: Full training and EDA workflow
- `app.py`: Interactive Streamlit dashboard
- `src/`: Core ML, data preprocessing, anomaly detection, and GenAI modules
- `Dockerfile` and `Procfile`: Deployment support files
- `docs/`: Project report, code explanation, and deployment guide
- `generate_presentation.py`: Creates a 15-slide presentation

## Prerequisites
- Python 3.9 or newer
- `pip` package manager
- Docker (optional for container deployment)

## Setup Instructions
1. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
2. Download the Rossmann dataset from Kaggle and place the files into the `data/` folder:
   - `train.csv`
   - `store.csv`
   - `test.csv` (optional)
3. Create an `.env` file with your Anthropic API key if you want AI insights:
   ```text
   ANTHROPIC_API_KEY=your_api_key_here
   ```

## Run the training pipeline
This pipeline performs data loading, preprocessing, EDA, and model training.
```bash
python run_pipeline.py
```

## Start the Streamlit dashboard
```bash
streamlit run app.py
```

## Generate the presentation
```bash
python generate_presentation.py
```

## Local deployment using Docker
Build the image:
```bash
docker build -t retail-demand-forecasting .
```
Run the container:
```bash
docker run -p 8501:8501 --env-file .env retail-demand-forecasting
```

## Project Structure
- `app.py`: Streamlit app for forecast simulation and AI insights
- `run_pipeline.py`: Trains models and generates EDA charts
- `requirements.txt`: Python dependencies
- `Dockerfile`: Container deployment instructions
- `Procfile`: Cloud process configuration
- `docs/`: Written project documentation
- `generate_presentation.py`: Creates the PowerPoint presentation

## Notes
- If the models are missing, run `python run_pipeline.py` first.
- The dashboard includes AI narrative sections that require the Anthropic API key.
- `src/` contains the reusable data and model logic.
