# Deployment Guide

This guide explains how to deploy the Retail Demand Forecasting app locally or in a cloud environment.

## Local Deployment

### Prerequisites
- Python 3.9+ installed
- `git` if cloning the repository
- `pip` available

### Setup
1. Install project dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
2. Download the Rossmann dataset from Kaggle and place files into `data/`:
   - `train.csv`
   - `store.csv`
   - `test.csv` (optional)
3. Create `.env` with your Anthropic API key:
   ```text
   ANTHROPIC_API_KEY=your_api_key_here
   ```

### Train the Models
Run the pipeline to train models and generate EDA outputs:
```bash
python run_pipeline.py
```
This saves model artifacts to `src/lr_model.joblib`, `src/rf_model.joblib`, and `src/features_list.joblib`.

### Start the Streamlit Dashboard
```bash
streamlit run app.py
```
Open the URL shown in your terminal (usually `http://localhost:8501`).

## Docker Deployment

### Build the Docker Image
```bash
docker build -t retail-demand-forecasting .
```

### Run the Container
```bash
docker run -p 8501:8501 --env-file .env retail-demand-forecasting
```

The app will be available at `http://localhost:8501`.

## Cloud Hosting

### Streamlit Community Cloud
1. Push this repository to GitHub.
2. Add `requirements.txt`, `app.py`, and `Dockerfile` to the root.
3. Create a Streamlit app in the cloud and link the GitHub repository.
4. Add `ANTHROPIC_API_KEY` as a secret environment variable.

### Heroku / Other PaaS
Use the provided `Procfile`:
```text
web: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

If deploying with Heroku, ensure `requirements.txt` includes all dependencies.

## Notes
- The app uses pre-trained model files in `src/`. If these are absent, run `python run_pipeline.py` first.
- If Anthropic credentials are unavailable, the app still runs but GenAI sections show informational fallbacks.
- For production, keep keys secure and avoid committing `.env` to source control.
