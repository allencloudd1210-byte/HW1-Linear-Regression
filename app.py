import io
from dataclasses import dataclass

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


st.set_page_config(page_title="HW1: Linear Regression", layout="wide")


@dataclass
class DataParams:
    slope: float
    intercept: float
    noise_std: float
    num_points: int
    random_seed: int


def generate_synthetic_data(params: DataParams) -> pd.DataFrame:
    rng = np.random.default_rng(params.random_seed)
    x_values = np.linspace(-10, 10, params.num_points)
    noise = rng.normal(0.0, params.noise_std, size=params.num_points)
    y_values = params.slope * x_values + params.intercept + noise
    return pd.DataFrame({"x": x_values, "y": y_values})


def fit_linear_regression(df: pd.DataFrame) -> tuple[LinearRegression, pd.Series]:
    model = LinearRegression()
    X = df[["x"]]
    y = df["y"]
    model.fit(X, y)
    predictions = pd.Series(model.predict(X), index=df.index, name="y_pred")
    return model, predictions


def compute_metrics(y_true: pd.Series, y_pred: pd.Series) -> dict:
    mse = mean_squared_error(y_true, y_pred)
    rmse = float(np.sqrt(mse))
    r2 = r2_score(y_true, y_pred)
    return {"MSE": mse, "RMSE": rmse, "R2": r2}


def sidebar_controls() -> tuple[DataParams, pd.DataFrame | None]:
    st.sidebar.header("Data Controls")
    slope = st.sidebar.slider("slope a", -5.0, 5.0, 1.5, 0.1)
    intercept = st.sidebar.slider("intercept b", -10.0, 10.0, 0.5, 0.1)
    noise_std = st.sidebar.slider("noise std", 0.0, 10.0, 2.0, 0.1)
    num_points = st.sidebar.slider("number of points n", 10, 400, 120, 1)
    random_seed = st.sidebar.number_input("random seed", min_value=0, value=42, step=1)

    st.sidebar.divider()
    st.sidebar.subheader("Upload CSV (optional)")
    uploaded = st.sidebar.file_uploader("CSV with columns x,y", type=["csv"]) 
    df_uploaded: pd.DataFrame | None = None
    if uploaded is not None:
        try:
            df_uploaded = pd.read_csv(uploaded)
            if not {"x", "y"}.issubset(df_uploaded.columns):
                st.sidebar.error("CSV must contain columns: x, y")
                df_uploaded = None
        except Exception as exc:
            st.sidebar.error(f"Failed to read CSV: {exc}")

    params = DataParams(
        slope=float(slope),
        intercept=float(intercept),
        noise_std=float(noise_std),
        num_points=int(num_points),
        random_seed=int(random_seed),
    )
    return params, df_uploaded


def main() -> None:
    st.title("HW1: Linear Regression")
    st.write("Follow CRISP-DM: business understanding → data → modeling → evaluation → deployment.")

    params, df_uploaded = sidebar_controls()

    with st.expander("Current parameters", expanded=False):
        st.json(params.__dict__)

    if df_uploaded is not None:
        df = df_uploaded.copy()
        st.info("Using uploaded dataset.")
    else:
        df = generate_synthetic_data(params)

    model, y_pred = fit_linear_regression(df)
    df_result = df.assign(y_pred=y_pred, residual=lambda d: d["y"] - d["y_pred"])

    metrics = compute_metrics(df_result["y"], df_result["y_pred"]) 

    col_left, col_right = st.columns([3, 2], gap="large")

    with col_left:
        st.subheader("Data and fitted line")
        fig = px.scatter(df_result, x="x", y="y", opacity=0.7, title="Observed data")
        line_x = np.array([df_result["x"].min(), df_result["x"].max()])
        line_y = model.coef_[0] * line_x + model.intercept_
        fig.add_traces(px.line(x=line_x, y=line_y).data)
        fig.update_traces(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Residuals")
        fig_res = px.scatter(df_result, x="x", y="residual", color=abs(df_result["residual"]).round(2),
                             labels={"color": "|residual|"})
        st.plotly_chart(fig_res, use_container_width=True)

    with col_right:
        st.subheader("Learned parameters")
        st.metric("slope a (coef)", f"{model.coef_[0]:.4f}")
        st.metric("intercept b", f"{model.intercept_:.4f}")

        st.subheader("Metrics")
        st.table(pd.DataFrame(metrics, index=["value"]).T)

        st.subheader("Data preview")
        st.dataframe(df_result.head(20), use_container_width=True)

        csv_buf = io.StringIO()
        df_result.to_csv(csv_buf, index=False)
        st.download_button(
            label="Download results CSV",
            data=csv_buf.getvalue().encode("utf-8"),
            file_name="linear_regression_results.csv",
            mime="text/csv",
        )

    st.caption(
        "Tip: Use the sidebar to adjust a, b, noise, n; or upload your own CSV with columns x,y."
    )


if __name__ == "__main__":
    main()


