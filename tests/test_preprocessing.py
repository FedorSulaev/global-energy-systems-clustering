import pandas as pd
from src.preprocess import load_data, feature_selection

def test_date_parsing():
    df = pd.DataFrame({'date': ['2023-01-01', None]})
    df = load_data("data/raw/global_electricity_production_data.csv")
    assert "year" in df.columns

def test_feature_selection():
    df = pd.DataFrame({
        "A": [1, 1, 1, 1],
        "B": [2, 2, 2, 2],
        "C": [1, 2, 3, 4],
        "D": [2, 4, 6, 8],
    })
    filtered = feature_selection(df, 0.01, 0.9)
    assert "D" not in filtered.columns
