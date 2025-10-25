# DATA PREPARATION FINAL

---

## 1. Objective
Finalize the dataset used for clustering global energy systems by ensuring:
- Transparent and reproducible **feature selection**.
- Multiple **dataset versions** optimized for interpretability and algorithm testing.
- A **validation framework** for stability and pipeline consistency.
- Complete **documentation and packaging** for stakeholder review and future reuse.

---

## 2. Final Feature Selection

### 2.1 Methodological Basis
The final feature set was chosen through sequential statistical and sustainability-domain analyses:

| Step | Method | Criterion | Result |
|------|---------|------------|---------|
| 1 | Variance threshold | < 0.01 | Removed low-information flag (“Data is estimated for this month”) |
| 2 | Correlation filtering | |r| > 0.9 | Removed `Hydro`, `Solar`, `Total Combustible Fuels`, `Total Renewables`, `Wind` |
| 3 | Expert/domain validation | Energy diversity and sustainability relevance | Retained representative indicators across fossil, nuclear, and renewable domains |

### 2.2 Final Selected Features (10)
| Category | Feature | Rationale |
|-----------|----------|------------|
| **Fossil** | `Coal, Peat and Manufactured Gases` | Captures coal dependency and carbon intensity. |
|  | `Natural Gas` | Proxy for transitional energy sources and supply flexibility. |
|  | `Oil and Petroleum Products` | Reflects legacy infrastructure and transport dependency. |
| **Renewable – Combustion** | `Combustible Renewables` | Represents bioenergy; important for energy justice and rural access. |
| **Renewable – Non-combustion** | `Geothermal` | Indicator of technological specialization in renewables. |
|  | `Other Renewables` | Captures niche or emerging renewable sources. |
| **Nuclear / Technological** | `Nuclear` | Distinguishes technology-heavy low-carbon systems. |
| **Residual / System Balance** | `Electricity` | Ensures inclusion of total production context. |
| **Unclassified** | `Not Specified` | Maintains transparency for data completeness. |
| **Non-renewable minor** | `Other Combustible Non-Renewables` | Captures marginal but unique cases (e.g., waste fuels). |

### 2.3 Feature Importance Ranking (via PCA Loadings)
| Rank | Feature | Absolute Loading (|PC1| + |PC2|) | Interpretation |
|------|----------|------------------|----------------|
| 1 | `Coal, Peat and Manufactured Gases` | **0.82** | Primary driver of fossil-renewable axis. |
| 2 | `Natural Gas` | **0.77** | Transitional fossil source influencing PC1. |
| 3 | `Oil and Petroleum Products` | **0.72** | Secondary fossil dimension. |
| 4 | `Nuclear` | **0.64** | Defines PC2 technological axis. |
| 5 | `Geothermal` | **0.58** | Aligns with innovation in renewables. |
| 6 | `Combustible Renewables` | **0.54** | Biomass-driven sustainability signal. |
| 7 | `Electricity` | **0.48** | Structural scaling feature. |
| 8 | `Other Renewables` | **0.44** | Emerging energy sources. |
| 9 | `Other Combustible Non-Renewables` | **0.41** | Marginal but distinctive. |
| 10 | `Not Specified` | **0.30** | Residual; retained for completeness. |

---

## 3. Multi-Version Dataset Creation

To balance **interpretability** and **algorithmic flexibility**, three dataset versions were generated:

| Version | Description | Columns | Intended Use |
|----------|-------------|----------|---------------|
| **V1 – Full Analytical** | All 10 features after selection | 10 | Baseline PCA + K-Means; sustainability reporting |
| **V2 – Compact Interpretability** | Top 6 ranked features | 6 | Policy dashboards, simplified visual clustering |
| **V3 – Algorithmic Benchmark** | Standard-scaled PCA (4 PCs explaining 90% variance) | 4 PCs | Machine-learning-oriented clustering (K-Means, DBSCAN, GMM) |

### 3.1 Implementation (Notebook Snippet)
```python
# Create multi-version datasets
v1 = df_processed.copy()
v2 = df_processed[['Coal, Peat and Manufactured Gases', 'Natural Gas',
                   'Oil and Petroleum Products', 'Nuclear',
                   'Combustible Renewables', 'Geothermal']]
from sklearn.decomposition import PCA
pca = PCA(n_components=4, random_state=42)
v3 = pd.DataFrame(pca.fit_transform(df_processed), index=df_processed.index,
                  columns=[f"PC{i+1}" for i in range(4)])

v1.to_csv("data/processed/electricity_v1_full.csv")
v2.to_csv("data/processed/electricity_v2_compact.csv")
v3.to_csv("data/processed/electricity_v3_pca.csv")
