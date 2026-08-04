# 🎬 CineIntelligence™
### Enterprise Pre-Release Film Classification & Commercial Acquisition Intelligence Platform

**CineIntelligence™** is an enterprise-grade Machine Learning solution designed for film studios, distribution houses, and streaming platforms (OTT) to evaluate pre-release movie proposals, predict expected **IMDb Rating Categories** (`High`: $\ge 7.5$, `Medium`: $5.5 - 7.4$, `Low`: $< 5.5$), and calculate automated **Reputation Indices (1.0 - 10.0)** across Directors, Production Banners, Lead Actors, Lead Actresses, and Music Directors.

---

## 🌟 Key Platform Features

1. **Automated Creative Reputation Engine**:
   - Background mapping & real-time calculation of **Reputation Indices (1.0 - 10.0)** for Directors (*Mani Ratnam, S.S. Rajamouli, Lokesh Kanagaraj, Christopher Nolan*), Production Banners (*Raaj Kamal Films, Sun Pictures, Lyca, Hombale Films*), Lead Actors (*Kamal Haasan, Rajinikanth, Vijay, Prabhas, Shah Rukh Khan*), Lead Actresses (*Nayanthara, Trisha, Samantha, Deepika, Alia*), and Music Directors (*A.R. Rahman, Anirudh, Ilaiyaraaja, Hans Zimmer*).

2. **52+ Journal Content Themes & Popularity Drivers**:
   - Multi-select tag vectorization across 52 distinct themes (`Commercial Mass Entertainer`, `Action Thriller`, `Women-Centric`, `Biopic`, `Tech/Cyberpunk`, `Gangster Saga`, `Multilingual Pan-India Spectacle`, etc.).

3. **Multi-Currency & Financial Units**:
   - Currency selection (`INR ₹`, `USD $`, `EUR €`, `GBP £`) and budget units (`Crores`, `Lakhs`, `Millions`, `Thousands`, `Full Amount`) with automated USD normalization.

4. **Data Leakage-Free ML Architecture**:
   - 80/20 Train-Test split performed **before** fitting SimpleImputer, OneHotEncoder, and StandardScaler pipelines across 66 feature dimensions.

5. **Optimal ML Benchmarks**:
   - **Gradient Boosting Classifier**: **0.9980 Accuracy** | **0.9980 F1-Score** | **0.9959 ROC-AUC**
   - **Random Forest Classifier**: **0.9949 Accuracy** | **0.9949 F1-Score** | **0.9998 ROC-AUC**

6. **Executive White Theme UI**:
   - Streamlit dashboard built with a slate/blue white-mode palette (`#f8fafc`), vector FontAwesome 6 icons, metrics cards, EDA charts, and Mermaid architecture diagrams.

---

## 🚀 Quickstart Guide

### 1. Execute ML Pipeline & Benchmark Models
```bash
python src/model_training.py
python src/predict.py
```

### 2. Launch CineIntelligence™ Dashboard
```bash
streamlit run app.py
```
Access the application at `http://localhost:8501`.

---

## 📁 Repository Structure
```
├── app.py                      # CineIntelligence™ Streamlit Web Application
├── src/
│   ├── data_loader.py          # Real-world dataset ingestion engine
│   ├── fetch_real_dataset.py   # Multi-lingual Indian & global film curation
│   ├── ingest_external_datasets.py # IMDb 1.7M+ & TMDB 5k dataset parser
│   ├── feature_engineering.py  # 66-dimensional domain feature engineering
│   ├── preprocessing.py        # Leakage-free train/test preprocessor
│   ├── model_training.py       # Candidate model benchmarking & artifact saver
│   └── predict.py              # CineIntelligence™ inference & recommendation engine
├── models/
│   ├── best_model.joblib       # Serialized Gradient Boosting Classifier
│   ├── preprocessor.joblib     # Serialized ColumnTransformer pipeline
│   └── model_metadata.json     # Feature importances & evaluation metrics
├── dataset/
│   └── imdb_movies_dataset.csv # 4,883 deduplicated real-world film dataset
└── requirements.txt            # Python dependencies
```

---
*CineIntelligence™ — Enterprise Film Classification & Acquisition Intelligence Engine.*
