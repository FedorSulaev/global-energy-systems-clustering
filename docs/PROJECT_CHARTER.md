## Clustering Approach Rationale

### Clustering Family Anticipated
**Partition-based clustering (K-Means and Hierarchical variants)**

---

### Rationale

1. **Data Nature**
   - The dataset represents approximately **150–200 countries**, each described by **percentage-based features** such as coal, gas, oil, hydro, nuclear, wind, solar, and biofuels.
   - Data is **low-dimensional, continuous, and normalized** (0–100%), making it suitable for **distance-based clustering** methods.
   - Dataset size is moderate, so **computational cost is low**, allowing for exploration of multiple algorithms and validations.

2. **Expected Cluster Geometry**
   - Countries are expected to form **distinct, globally separable, convex clusters** (e.g., fossil-heavy, renewable-dominant, hydro/nuclear-dependent).
   - **K-Means** is effective for such compact, Euclidean-shaped clusters.
   - **Hierarchical clustering (Ward’s linkage)** will be used to validate stability and visualize relationships among clusters.

3. **Impact Objectives**
   - The objective is to **create interpretable, actionable groupings** of national energy systems that can guide differentiated decarbonization and investment strategies.
   - Partition-based methods yield **centroids that serve as representative archetypes**, aligning with the need for **policy transparency and benchmarking**.
   - **Soft clustering (Gaussian Mixture Models)** may be considered later to capture “transitioning” countries that share characteristics across clusters.

4. **Why Not Other Methods**
   - **Density-based (DBSCAN/HDBSCAN):** Not appropriate since data lacks local density variation and noise.
   - **Spectral clustering:** Unnecessary for small, low-dimensional data; adds complexity without interpretive gain.
   - **Model-based clustering:** Reserved for future work incorporating temporal or policy metrics.

---

### Summary

| **Criterion** | **Choice** | **Reason** |
|----------------|------------|-------------|
| **Clustering family** | Partition-based (K-Means, Hierarchical) | Numeric, small dataset, interpretable centroids |
| **Expected cluster shape** | Compact / convex | Countries with similar % energy mix |
| **Impact alignment** | High interpretability for policy segmentation | Enables actionable sustainability insights |
| **Backup option** | Gaussian Mixture (soft clustering) | For overlapping transition-state countries |

---

**In summary:**  
The project will begin with **K-Means clustering** (validated with silhouette and Davies–Bouldin scores) to identify 4–6 archetypes of national electricity-generation systems. Results will directly support **SDG 7 (Affordable & Clean Energy)** and **SDG 13 (Climate Action)** by informing tailored energy-transition strategies.