# Runbook

## Run locally
```bash
cd /Users/bibi/Desktop/HM
pip install -r requirements.txt
streamlit run app.py
```

- Headless/background (optional):
```bash
streamlit run app.py --server.headless true --server.port 8502
```

## Troubleshooting
- ImportError about `pyarrow ... libarrow.*.dylib`:
  - We pin `pyarrow==16.1.0` which bundles needed libs. Reinstall deps:
  ```bash
  pip install --no-cache-dir --force-reinstall -r requirements.txt
  ```
- Port already in use:
  - Run on another port: `--server.port 8503`.
- Slow file watching on macOS:
  - Install watchdog for better performance:
  ```bash
  xcode-select --install
  pip install watchdog
  ```

## Deploy (Streamlit Cloud)
1. Push repo to GitHub.
2. In Streamlit Cloud, create new app pointing to `app.py`.
3. Set Python version 3.10+ and use this repo's `requirements.txt`.
4. Deploy. Verify sidebar controls, plots, metrics, CSV upload/download.
