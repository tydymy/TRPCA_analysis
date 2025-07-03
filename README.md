# TRPCA_analysis
# Chronological Age Estimation from Human Microbiomes with TRPCA

## Overview  
This repository contains the results and code for **Transformer-based Robust Principal Component Analysis (TRPCA)**, a deep-learning framework for predicting chronological age from skin, oral and gut microbiome profiles (16S rRNA and WGS). TRPCA leverages RPCA for dimensionality reduction and a lightweight transformer encoder for regression and multi-task learning, offering both accuracy gains and feature-level interpretability.

---

## Key Results

| Body Site / Data Type | Baseline MAE | TRPCA MAE | Improvement |
|-----------------------|--------------|-----------|-------------|
| Skin (16S)            | 5.73 ± 1.25  | 5.09 ± 1.07  | 14 %        |
| Skin (WGS)            | 11.14 ± 2.65 | 8.03 ± 4.10  | 28 %        |
| Oral (16S)            | 7.47 ± 2.05  | 7.02 ± 1.82  | 6 %         |
| Oral (WGS)            | 7.16 ± 0.69  | 6.72 ± 0.81  | 6 %         |
| Gut (16S)             | 11.66 ± 0.36 | 11.42 ± 0.55 | 2 %         |
| Gut (WGS)             | 9.98 ± 0.80  | 8.83 ± 0.50  | 12 %        |

**Multi-Task Learning (WGS gut)**  
- **Age prediction:** MAE 10.86 → 10.21 years (6 % ↓)  
- **Birth-country classification:** 79 % → 89 % accuracy (13 % ↑)

---

## Data & Code Availability

* **16S datasets**: [https://github.com/shihuang047/age-prediction](https://github.com/shihuang047/age-prediction)
* **WGS datasets**: [https://waldronlab.io/curatedMetagenomicDataAnalyses/articles/MLdatasets.html](https://waldronlab.io/curatedMetagenomicDataAnalyses/articles/MLdatasets.html)
* **Analysis notebooks**: [https://github.com/tydymy/TRPCA\_analysis](https://github.com/tydymy/TRPCA_analysis)
* **Model code**: [https://github.com/tydymy/TRPCA](https://github.com/tydymy/TRPCA)

