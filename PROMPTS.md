# Prompt & Process Log

This file records key prompts and decisions during development.

## Steps taken (chronological)
1. Scaffolded project: created `README.md`, `requirements.txt`, `app.py` minimal Streamlit app.
2. Implemented features: adjustable `a, b, noise, n`, synthetic data generation, OLS fit, metrics (MSE, RMSE, R2), plots (scatter+line, residuals), CSV upload/download.
3. Wrote `CRISP_DM.md` per assignment requirements.
4. Documented initial prompts and design choices.
5. Installed dependencies; encountered `ModuleNotFoundError: sklearn` -> installed via `pip install -r requirements.txt`.
6. Ran app; hit `pyarrow` dylib error on macOS. Solution: pinned `pyarrow==16.1.0` and reinstalled with `--no-cache-dir --force-reinstall`.
7. Launched app on port 8502 in headless mode to verify.
8. Added documentation: `GOAL.md`, `CHANGELOG.md`, `RUNBOOK.md`.

## Design choices
- Use scikit-learn `LinearRegression` for clarity.
- Plotly for interactive visuals; Streamlit for UI.
- Keep code readable with dataclass for parameters.
- CSV schema check: require columns `x,y`.
