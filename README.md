# Interactive Linear Regression Visualizer

This is a Streamlit web application that lets you interactively visualize linear regression. Adjust the number of points, slope/intercept, and noise to see how the fitted line and residuals change. You can also upload a CSV with columns `x,y` and download the results.

## Demo Site
The app can be deployed on Streamlit Cloud. Example (replace with your deployed URL):

- `https://aiotda.streamlit.app/`

## Project Summary
This project was developed to provide an interactive tool for understanding linear regression. It includes:

- A Streamlit UI with controls for `a`, `b`, `n`, and noise
- Synthetic data generation and optional CSV upload
- OLS fitting (scikit-learn `LinearRegression`) and metrics (MSE, RMSE, R2)
- Plots: scatter + fitted line, residual plot
- CRISP-DM write-up and prompt/process log

## Development Log
For a chronological list of actions taken, see `CHANGELOG.md`. Key milestones include:

1. Initial setup and app creation (`app.py`, `requirements.txt`, docs)
2. Feature implementation and validation of the project plan
3. Troubleshooting run-time issues (pinned `pyarrow==16.1.0` on macOS)
4. Successful local runs and documentation updates

## To-Do List for Linear Regression Implementation (outline)
High-level steps typically involved when implementing linear regression end-to-end:

1. Data Preparation
   - Load dataset (CSV/NumPy)
   - Handle missing values (if any)
   - Optional split train/test; optional scaling
2. Model Implementation
   - Use scikit-learn `LinearRegression` (or implement from scratch if required)
   - Define hypothesis and cost (MSE) if doing from scratch
3. Training
   - Fit model and monitor convergence/metrics if training loop exists
4. Evaluation
   - Compute MSE, RMSE, R2; visualize predictions vs. actuals
5. Prediction
   - Provide a function or UI to predict on new data
6. Documentation and Reporting
   - Document code and write a short report of results and conclusions

## Quickstart (Local)

1. Create/activate Python 3.10+ environment
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Files

- `app.py` — Streamlit application
- `requirements.txt` — Python dependencies
- `CRISP_DM.md` — CRISP-DM process write-up
- `PROMPTS.md` — prompt/process log
- `GOAL.md` — project objectives and acceptance criteria
- `CHANGELOG.md` — step-by-step actions taken
- `RUNBOOK.md` — how to run, troubleshoot, deploy

## Deployment

The app is ready for Streamlit Cloud. Push this repo to GitHub and deploy.


