# Feature Selection Documentation
## Capstone Project: Global Energy Clustering for Sustainable Development

### 1. Objective
Enhance clustering interpretability by selecting features that maximize information diversity while reducing redundancy and noise in global electricity production data.

---

### 2. Methods and Rationale

| Step | Technique | Purpose | Implementation | Result |
|------|------------|----------|----------------|--------|
| **Variance Thresholding** | Remove low-variance features | Eliminate variables with minimal discriminative power | Threshold = 0.01 | Removed `Data is estimated for this month` |
| **Correlation Filtering** | Reduce redundancy | Drop features with |r| > 0.9 | Correlation matrix and pair filtering | Removed `Hydro`, `Solar`, `Total Combustible Fuels`, `Total Renewables`, `Wind` |
| **PCA Validation** | Assess dimensional compactness | Evaluate explained variance ratio | 4 PCs explain 90% variance | Confirms dimensional efficiency |

---

### 3. Expert Validation
Energy domain guidelines (IEA, UN SDG 7, IPCC AR6) informed the selection process:

- Maintain **balanced representation** across fossil, nuclear, and renewable categories.
- Avoid dropping features central to sustainability narratives (e.g., `Nuclear`, `Other Renewables`).
- Verify interpretability: retained features map to clear, policy-relevant energy types.

**Validated feature set (10 total):**
['Coal, Peat and Manufactured Gases',
'Combustible Renewables',
'Electricity',
'Geothermal',
'Natural Gas',
'Not Specified',
'Nuclear',
'Oil and Petroleum Products',
'Other Combustible Non-Renewables',
'Other Renewables']


---

### 4. Quantitative Impact
| Metric | Before Selection | After Selection | Δ Impact |
|---------|------------------|-----------------|-----------|
| Features | 16 | 10 | −6 redundant |
| Variance Explained (PCA) | 90% → 5 components | 90% → 4 components | More compact representation |
| Silhouette Score | 0.652 | **0.685** | Improved cluster separability |

Feature selection improved both **statistical efficiency** and **interpretive clarity**, demonstrating that redundancy reduction enhanced the clustering process without loss of domain validity.

---

### 5. Interpretability & Sustainability Implications
- The final feature set captures structural diversity across global energy systems.
- It balances **quantitative optimization** with **qualitative transparency**.
- Each retained variable corresponds to a **sustainability lever** — fossil dependence, renewable integration, or technological specialization.

---

### 6. Conclusion
The systematic feature selection process:
- Simplified the dataset from 16 → 10 variables.
- Enhanced clustering stability and meaning.
- Preserved interpretability aligned with energy transition frameworks.

This final feature subset forms the foundation for the PCA and clustering analyses used to derive **energy system archetypes** across 48 countries.

