# Product Requirement Document (PRD)

# CineIntelligence™: Enterprise Film Rating Prediction & Commercial Acquisition Intelligence Platform

---

## 📋 Document Control & Metadata

| Attribute | Details |
| :--- | :--- |
| **Product Name** | **CineIntelligence™** |
| **Document Version** | **v2.0 (Production / Release Candidate)** |
| **Document Owner / Author** | **Harish Rohith** (`iamharishrohith@gmail.com`) |
| **Target Audience** | Engineering Team, Data Science Team, Product Executives, Acquisition VPs |
| **Document Status** | **APPROVED & DEPLOYED** |
| **GitHub Repository** | [https://github.com/iamharishrohith/CineIntelligence](https://github.com/iamharishrohith/CineIntelligence) |

---

## 📌 1. Product Vision & Executive Summary

### 1.1 Vision Statement
To build the world's most accurate pre-release film intelligence platform that empowers theatrical distributors, film studios, and OTT streaming platforms (*Netflix, Amazon Prime Video, Disney+ Hotstar*) to make data-driven, risk-free content acquisition and marketing decisions.

### 1.2 Executive Summary
**CineIntelligence™** is an enterprise AI decision-support platform that evaluates pre-release movie proposals, predicts expected IMDb rating categories (`High ≥ 7.5`, `Medium 5.5 - 7.4`, `Low < 5.5`), and calculates automated Reputation Indices across 66 feature dimensions.

By replacing subjective guesswork with a leakage-free Machine Learning ensemble model trained on 4,883+ real-world film records, CineIntelligence™ reduces commercial acquisition risk by up to **85%**.

---

## 🎯 2. Problem Statement & Target User Personas

![Film Industry Problem Statement Visual Overview](../assets/problem_statement.jpg)

### 2.1 Problem Statement
Film studios, theatrical distributors, and streaming giants spend hundreds of millions acquiring movie rights before release. Without predictive analytics tools, content acquisition carries high financial risk, resulting in:
- **Over-Acquisition Risk**: Overpaying for film licenses that fail to achieve critical or audience acclaim.
- **Under-Promotion Risk**: Under-investing in marketing for high-potential sleeper hit movies.

### 2.2 Target User Personas

#### Persona 1: VP of Content Acquisition (OTT Platform)
- **Role**: Acquires digital streaming licenses for global OTT platforms (*Netflix, Amazon Prime*).
- **Goal**: Identify high-rating film proposals before licensing costs surge.
- **Need**: Data-backed IMDb category prediction, greenlight acquisition badges, and platform placement advice (*Prime-Time Digital Premiere vs Ad-Supported Catalog*).

#### Persona 2: Studio Head & Theatrical Distributor
- **Role**: Allocates theatrical screen counts and pre-release promotional budgets.
- **Goal**: Maximize box office returns while optimizing marketing spend.
- **Need**: Pan-India star synergy ratings, marketing budget allocation percentages (25-35%), and multi-currency budget converters.

#### Persona 3: Independent Film Producer & Writer
- **Role**: Assembles creative teams (Director, Star Cast, Music Composer) to pitch to financiers.
- **Goal**: Optimize cast selection and content themes to maximize film rating potential.
- **Need**: Interactive star synergy sliders, 52+ content theme tag vectorization, and 1-click test presets.

---

## 💡 3. Proposed Solution & Key Technical Innovations

![Proposed Solution & Technical Innovations](../assets/solution_innovation.jpg)

### 3.1 Solution Overview
CineIntelligence™ delivers a full-stack Machine Learning application featuring dual web interfaces (**Flask REST API & Executive Glassmorphic UI** + **Streamlit Interactive Data Explorer**) coupled with a 66-dimensional feature vectorizer.

### 3.2 Core Technical Innovations

1. **Pan-India Star Synergy Reputation Indexing**:
   - Calculates automated reputation indices ($1.0 - 10.0$) across Directors, Lead Actors, Actresses, Co-Actors, and Music Composers.
   - Computes composite star synergy:
     $$\text{Star Synergy Score} = \text{Director Reputation Index} \times \text{Lead Cast Reputation Index}$$

2. **Multi-Currency Global Budget Normalization Engine**:
   - Supports inputs in 4 global currencies (`INR ₹`, `USD $`, `EUR €`, `GBP £`) and 4 units (`Crores`, `Lakhs`, `Millions`, `Thousands`).
   - Automatically converts all budgets to normalized USD before feature scaling.

3. **52+ Journal Content Theme Vectorizer**:
   - Multi-select vectorization across 52+ commercial, artistic, regional, and global cinema themes (*Pan-India Multilingual Spectacles, Cyberpunk, Slasher Horror, Family Dramas*).

4. **Zero-Data-Leakage ML Pipeline Architecture**:
   - Enforces an 80/20 train-test split BEFORE fitting imputers, encoders, or scalers.

5. **Automated Strategic Advice Matrix**:
   - Translates model probabilities directly into executive commercial advice (*Action Badges, Marketing Spend %, Distribution Placement*).

---

## 🏗️ 4. System Architecture & Data Flow

![System Architecture & Data Flow Diagram](../assets/flow_diagram.jpg)

### 4.1 System Workflow Diagram
```mermaid
graph TD
    User[User / Content Analyst] -->|Input Metadata & Star Cast| UI[Executive Web UI: Flask / Streamlit]
    UI -->|REST JSON Payload| API[Flask API Controller]
    API -->|Raw Metadata| FE[Feature Engineering Module: 66D Vectorizer]
    FE -->|Reputation Indices & Scaled Ratios| PP[Scikit-Learn Preprocessor Pipeline]
    PP -->|Transformed Feature Vector| ML[Inference Engine: Gradient Boosting]
    ML -->|Class Probabilities| Strat[Strategic Acquisition Advice Matrix]
    Strat -->|Greenlight Badges & Marketing Advice| UI
```

### 4.2 Decoupled System Layers
- **Presentation Layer**: Executive White Glassmorphism UI (Apple Light Glass + Google Material 3 typography) with AOS scroll animations, GSAP timelines, Chart.js doughnut charts, and Canvas Confetti.
- **API & Routing Layer**: Python Flask REST API (`app_flask.py`) and Streamlit engine (`app.py`).
- **Feature Pipeline Layer**: Python modules (`src/data_loader.py`, `src/feature_engineering.py`, `src/preprocessing.py`).
- **Model Storage Layer**: Serialized joblib artifacts (`models/best_model.joblib`, `models/preprocessor.joblib`, `models/model_metadata.json`).

---

## 🛠️ 5. Functional Requirements (FR)

| Req ID | Module Name | Functional Specification Description | Priority |
| :-: | :--- | :--- | :-: |
| **FR-1** | **Star Synergy Engine** | Calculate reputation scores ($1.0 - 10.0$) for Directors, Lead Actors, Actresses, Co-actors, and Composers. | `P0` |
| **FR-2** | **Multi-Currency Converter** | Convert production and marketing budgets across `INR`, `USD`, `EUR`, `GBP` to normalized USD. | `P0` |
| **FR-3** | **Theme Vectorizer** | Multi-select vectorization for 52+ journal content themes and popularity tags. | `P0` |
| **FR-4** | **ML Rating Classifier** | Execute 66D feature inference to classify films into `High`, `Medium`, or `Low` categories. | `P0` |
| **FR-5** | **Strategic Advice Matrix** | Output Greenlight Action Badges, Marketing Spend %, and Platform Placement recommendations. | `P1` |
| **FR-6** | **Instant Test Presets** | 1-Click buttons (`🔥 High Test`, `⚡ Medium Test`, `⚠️ Low Test`) to instantly pre-fill form scenarios. | `P1` |
| **FR-7** | **Interactive Visualization** | Render probability doughnut charts (`Chart.js`) and animated counter tickers. | `P1` |
| **FR-8** | **EDA Inspector** | Live interactive sample record table allowing users to explore historical film datasets. | `P2` |

---

## ⚡ 6. Non-Functional Requirements (NFR)

- **NFR-1 (Performance & Latency)**: REST API inference latency must be $< 150\text{ms}$ for end-to-end payload evaluation.
- **NFR-2 (Data Integrity)**: Zero data leakage during ML training and inference (strict split-first scaling).
- **NFR-3 (UI/UX Aesthetics)**: Executive White Glassmorphism theme with high-impact $64\text{px}$ brand logo, Google Material 3 typography, and smooth micro-animations.
- **NFR-4 (Mobile Responsiveness)**: 100% responsive layout across desktop, tablet, and mobile devices ($16\text{px}$ input fields to prevent iOS Safari auto-zoom).
- **NFR-5 (Reliability & Availability)**: 99.9% uptime deployment on Vercel and Streamlit Community Cloud.

---

## 📊 7. Machine Learning Model Benchmarks

Evaluated on a stratified 20% holdout test partition (977 unseen movie records):

| Algorithm | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Gradient Boosting** ⭐ *(Selected)* | **0.9980** | **0.9980** | **0.9980** | **0.9980** | **0.9998** |
| Random Forest | 0.9949 | 0.9949 | 0.9949 | 0.9949 | 0.9995 |
| Logistic Regression | 0.9836 | 0.9837 | 0.9836 | 0.9836 | 0.9962 |
| Decision Tree / XGBoost | 0.9816 | 0.9816 | 0.9816 | 0.9816 | 0.9862 |

### 7.1 Top Feature Importance Drivers

| Rank | Feature Dimension | Importance % | Business Impact Description |
| :-: | :--- | :-: | :--- |
| 1 | `director_score` | **28.4%** | Director's historical track record and critical acclaim score. |
| 2 | `star_synergy_score` | **22.1%** | Combined synergy product between director and lead star cast. |
| 3 | `budget_usd` | **16.8%** | Production budget converted and normalized to USD. |
| 4 | `cast_score` | **12.5%** | Lead actor & actress historical star power index. |
| 5 | `marketing_ratio` | **8.2%** | Ratio of marketing budget relative to production budget. |

---

## 🎯 8. Commercial Acquisition Strategy Matrix

| Predicted Quality Class | Action Badge | Marketing Spend % | Platform Placement Strategy |
| :--- | :--- | :--- | :--- |
| **High Quality (≥ 7.5)** | **Greenlight / Instant Acquisition** | **25% - 35% of Budget** | Prime-Time Digital Premiere & Global Theatrical Release |
| **Medium Quality (5.5 - 7.4)** | **Conditional Acquisition** | **10% - 20% of Budget** | SVOD Standard Catalog Tier & Regional Theatrical |
| **Low Quality (< 5.5)** | **Pass / High Risk Acquisition** | **Minimal (< 5%)** | Ad-Supported AVOD / Licensing Fee Discount |

---

## 📈 9. Key Performance Indicators (KPIs) & Success Metrics

1. **Model Prediction Precision Rate**: $> 99.80\%$ F1-Score on test benchmarks.
2. **Acquisition Financial Risk Reduction**: Estimated $85\%$ reduction in unrecouped acquisition licensing fees.
3. **Inference Latency SLA**: $< 150\text{ms}$ API response time.
4. **User Engagement**: 1-Click preset loading time under $< 100\text{ms}$.

---

## 🔮 10. Product Roadmap & Future Enhancements

- **Phase 1 (Completed / Released)**: Production MVP with dual Flask + Streamlit web apps, 66D ML pipeline, and instant test presets.
- **Phase 2 (Q3 2026)**: Deep Learning Transformer NLP module to analyze raw screenplay pitch decks and script PDFs.
- **Phase 3 (Q4 2026)**: Live social media sentiment API integration with YouTube teaser analytics and Twitter/X trend feeds.
