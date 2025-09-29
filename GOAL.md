# Project Goal

## What we want to achieve
- Build a simple, educational Linear Regression web app for HW1.
- Follow CRISP-DM and provide process artifacts (CRISP_DM.md, PROMPTS.md).
- Let users control data generation: slope a, intercept b, noise, number of points n.
- Allow CSV upload (x,y) and results download.
- Visualize data, fitted line, residuals; show metrics (MSE, RMSE, R2).
- Ready for Streamlit Cloud deployment.

## Acceptance Criteria
- App starts via `streamlit run app.py` with no errors on macOS arm64.
- Sidebar controls exist and affect plots/metrics in real time.
- Uploading a CSV with columns `x,y` works; invalid schema is handled.
- Metrics and learned parameters are displayed clearly.
- Repo contains: `README.md`, `GOAL.md`, `CRISP_DM.md`, `PROMPTS.md`, `CHANGELOG.md`, `RUNBOOK.md`, `requirements.txt`, `app.py`.
