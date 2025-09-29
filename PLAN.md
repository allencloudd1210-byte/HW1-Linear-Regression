# Implementation Plan (Initial)

## Objectives
- Build an interactive Streamlit app that demonstrates simple linear regression end-to-end.
- Provide CRISP-DM artifacts and a clear development process trail.

## Scope
- Data: synthetic generator `y = a*x + b + noise`; CSV upload with `x,y`.
- Modeling: scikit-learn `LinearRegression`.
- UI: Sidebar controls for `a, b, n, noise`; plots, metrics, CSV download.
- Docs: README, GOAL, PLAN, CRISP_DM, PROMPTS, CHANGELOG, RUNBOOK.

## Milestones
1) Scaffold
   - Create repo structure
   - Add `requirements.txt`, `README.md`, `app.py` skeleton
2) Core functionality
   - Dataclass for parameters; synthetic data function
   - Fit OLS; compute MSE, RMSE, R2
   - Plots: scatter + fitted line, residuals
3) UX features
   - Sidebar controls; expander for current params
   - CSV upload (validate `x,y`); results CSV download
4) Documentation
   - `CRISP_DM.md`, `PROMPTS.md`, `GOAL.md`, `PLAN.md`
   - `CHANGELOG.md`, `RUNBOOK.md`
5) Stabilization
   - Pin critical deps (e.g., `pyarrow==16.1.0` for macOS)
   - Smoke test on local and prepare for Streamlit Cloud
6) Deployment (optional)
   - Push to GitHub; configure Streamlit Cloud app

## Risks & Mitigations
- pyarrow/libarrow on macOS: pin to 16.1.0 and reinstall with `--no-cache-dir`.
- CSV schema variance: enforce `x,y` columns with clear error messages.
- Performance on large `n`: cap slider; use Plotly for efficient rendering.

## Acceptance Criteria (summary)
- App runs locally without errors; UI updates plots/metrics live.
- CSV upload/download works; metrics and parameters visible.
- Docs present and up to date.
