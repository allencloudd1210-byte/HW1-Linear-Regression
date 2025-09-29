# Changelog

All notable changes and actions taken in this project.

## 2025-09-29
- Init repo: add `README.md`, `requirements.txt`, `app.py` with Streamlit LR app.
- Add `CRISP_DM.md` documenting CRISP-DM steps.
- Add `PROMPTS.md` to log prompts/decisions.
- Fix runtime error: pin `pyarrow==16.1.0` to resolve `libarrow.1800.dylib` import error.
- Reinstall dependencies with `--no-cache-dir --force-reinstall`.
- Launch Streamlit on port 8502 to verify service.
- Add documentation files: `GOAL.md`, `CHANGELOG.md`, `RUNBOOK.md`.
