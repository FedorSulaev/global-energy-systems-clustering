# Preprocessing Pipeline Documentation

## 1. Objective
Ensure transparent, reproducible, and validated preprocessing for the **Global Energy Clustering Dataset** used in sustainability analytics.

---

## 2. Workflow Overview
1. **Data Loading:** Import raw CSV file, parse date fields.
2. **Cleaning:** Drop missing or invalid dates.
3. **Aggregation:** Group by country and product for the latest year.
4. **Pivoting:** Convert data to wide format (country × energy features).
5. **Feature Selection:** Apply variance thresholding and correlation filtering.
6. **Scaling:** Standardize feature magnitudes.
7. **Output:** Save a clean, ready-to-cluster CSV to `data/processed/`.

---

## 3. Configuration
All settings are controlled via `config/preprocessing_config.yaml`, including:
- Input/output paths
- Feature thresholds
- Aggregation year
- Random seed

This ensures **parameter transparency** and full **reproducibility**.

---

## 4. Usage

### Run from Terminal
```bash
python src/preprocess.py
