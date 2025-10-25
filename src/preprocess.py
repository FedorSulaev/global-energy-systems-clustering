"""
preprocess.py
-------------
Preprocessing pipeline for Global Energy Clustering Dataset.

Steps:
1. Load raw data.
2. Parse and clean date columns.
3. Aggregate monthly to yearly data.
4. Pivot to country-feature matrix.
5. Handle missing values.
6. Apply variance and correlation-based feature selection.
7. Save processed dataset for downstream clustering.

Author: Fedor Sulaev
Date: October 2025
"""

import pandas as pd
import numpy as np
import yaml
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import StandardScaler

def load_config(path="config/preprocessing_config.yaml"):
    """Load YAML configuration file."""
    with open(path, "r") as file:
        return yaml.safe_load(file)

def load_data(input_path: str) -> pd.DataFrame:
    """Load dataset and parse dates."""
    df = pd.read_csv(input_path)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    return df

def aggregate_latest_year(df: pd.DataFrame, latest_year: int) -> pd.DataFrame:
    """Aggregate to the latest available year."""
    df_year = df[df["year"] == latest_year]
    pivot = (
        df_year.pivot_table(
            index="country_name",
            columns="product",
            values="value",
            aggfunc="sum",
        )
    )
    pivot = pivot.fillna(0)
    return pivot

def feature_selection(df: pd.DataFrame, var_thresh: float, corr_thresh: float) -> pd.DataFrame:
    """Apply variance and correlation-based feature filtering."""
    selector = VarianceThreshold(threshold=var_thresh)
    X_var = selector.fit_transform(df)
    selected_cols = df.columns[selector.get_support()]
    df_filtered = df[selected_cols]

    corr_matrix = df_filtered.corr().abs()
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    to_drop = [col for col in upper.columns if any(upper[col] > corr_thresh)]
    df_final = df_filtered.drop(columns=to_drop)

    print(f"Removed due to high correlation: {to_drop}")
    print(f"Final selected features: {list(df_final.columns)}")
    return df_final

def scale_features(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize features."""
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df)
    return pd.DataFrame(scaled, columns=df.columns, index=df.index)

def run_pipeline(config_path="config/preprocessing_config.yaml"):
    """Main pipeline execution."""
    cfg = load_config(config_path)
    df = load_data(cfg["data"]["input_path"])
    print(f"Raw dataset loaded with {len(df)} records.")

    df_pivot = aggregate_latest_year(df, cfg["processing"]["latest_year"])
    print(f"Aggregated dataset shape: {df_pivot.shape}")

    df_selected = feature_selection(
        df_pivot,
        var_thresh=cfg["thresholds"]["variance"],
        corr_thresh=cfg["thresholds"]["correlation"]
    )

    df_scaled = scale_features(df_selected)
    df_scaled.to_csv(cfg["data"]["output_path"])
    print(f"✅ Preprocessing complete. Saved to {cfg['data']['output_path']}")

if __name__ == "__main__":
    run_pipeline()
