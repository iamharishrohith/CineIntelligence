# 🚨 Hackathon On-the-Spot Quick-Response Playbook

This document is your **emergency cheat sheet** for making rapid code modifications on the spot during a live hackathon evaluation. Use the search commands below to locate the precise code locations.

---

## 🎛️ 1. Star Reputation & Synergy Modifiers

### 1.1 Modifying Reputation Map Mappings
If an evaluator asks: *"What if [Name] is rated higher/lower in your system?"*

*   **Location**: [`src/predict.py`](file:///c:/Users/kevin/Documents/Harish%20Rohith/ML/src/predict.py#L15-L56)
*   **Search Target**: `DIRECTOR_REPUTATION_MAP`, `ACTOR_REPUTATION_MAP`, `MUSIC_REPUTATION_MAP`
*   **How to change**: Simply change the dictionary float values (e.g., change `9.8` to `10.0` or add a new entry):
    ```python
    DIRECTOR_REPUTATION_MAP = {
        "s.s. rajamouli": 9.8,  # Change to 10.0 if requested
        "new director": 8.5    # Add new entries dynamically
    }
    ```

### 1.2 Adjusting Star Synergy Weight Coefficient
If asked: *"How do you calculate synergy? Can we make the director's weight even higher than the cast's?"*

*   **Location**: [`src/feature_engineering.py`](file:///c:/Users/kevin/Documents/Harish%20Rohith/ML/src/feature_engineering.py#L52-L54)
*   **Search Target**: `star_synergy_score`
*   **How to change**: Tweak the synergy equation:
    ```python
    # Default: Director score * Cast score * Music score multiplier
    df['star_synergy_score'] = df['director_score'] * cast_filled * (df['music_score'] / 7.5)
    
    # Alternative (Giving Director 2x weight):
    df['star_synergy_score'] = (df['director_score'] * 2.0) * cast_filled
    ```

---

## ⚖️ 2. Business Matrix & Decision Thresholds

### 2.1 Tweaking Action Badges & Recommendations
If asked: *"Can you change the marketing allocation spend parameters for High-Tier movies to 30-40%?"*

*   **Location**: [`src/predict.py`](file:///c:/Users/kevin/Documents/Harish%20Rohith/ML/src/predict.py#L187-L202)
*   **Search Target**: `_generate_recommendation`
*   **How to change**: Modify the return string templates directly:
    ```python
    if category == 'High':
        tier = "Tier-1 Premium Acquisition"
        # Edit string here:
        marketing_advice = f"Allocate strong pre-release campaign (30-40% of {curr_symbol}{prod_val:.1f} {unit} budget)." 
    ```

---

## 💸 3. Multi-Currency & FX Exchange Rates

### 3.1 Updating Hardcoded Exchange Rates
If asked: *"The exchange rate for INR is outdated. Update it to 0.0118."*

*   **Location**: [`src/predict.py`](file:///c:/Users/kevin/Documents/Harish%20Rohith/ML/src/predict.py#L100-L105)
*   **Search Target**: `exchange_rates_to_usd`
*   **How to change**: Update the dictionary float values:
    ```python
    exchange_rates_to_usd = {
        'INR (₹)': 0.0118,  # Modified from 0.012
        'USD ($)': 1.0,
        'EUR (€)': 1.08,
        'GBP (£)': 1.28
    }
    ```

---

## 🏷️ 4. Adding / Modifying Content Themes

### 4.1 Step 1: Add to Frontend Dropdown Selection
If asked: *"Can we check specifically for 'AI Sci-Fi' theme?"*

*   **Location**: [`templates/app.html`](file:///c:/Users/kevin/Documents/Harish%20Rohith/ML/templates/app.html) or Streamlit lists in `app.py`
*   **Search Target**: `content_themes` / `<div class="theme-checkbox-grid">`
*   **How to change**: Add a new checkbox input tag:
    ```html
    <label class="checkbox-label">
        <input type="checkbox" name="content_themes" value="AI Sci-Fi"> AI Sci-Fi
    </label>
    ```

### 4.2 Step 2: Add to Feature Engineering vectorizer
*   **Location**: [`src/feature_engineering.py`](file:///c:/Users/kevin/Documents/Harish%20Rohith/ML/src/feature_engineering.py#L77-L88)
*   **Search Target**: `df['has_tech_scifi']`
*   **How to change**: Add binary column indicators:
    ```python
    df['has_ai_scifi'] = df['content_themes'].apply(lambda t: 1 if isinstance(t, list) and any('AI' in str(x) for x in t) else 0)
    ```

---

## 🎨 5. UI Customizations & Visual Styles

### 5.1 Changing Main Theme Accents (Executive Colors)
If asked: *"Can we see a version with an Emerald/Green brand accent instead of Blue?"*

*   **Location**: [`static/css/style.css`](file:///c:/Users/kevin/Documents/Harish%20Rohith/ML/static/css/style.css)
*   **Search Target**: `:root` variables
*   **How to change**: Edit color variables on spot:
    ```css
    :root {
        /* Default Blue: #2563eb */
        --primary: #10b981;       /* Change to Emerald Green */
        --primary-hover: #059669; /* Darker green */
        --primary-glow: rgba(16, 185, 129, 0.15);
    }
    ```

---

## 🧪 6. Fast Local Rebuild & Deployment Commands

| Operation | Command (Run in root folder) | Why / When to use |
| :--- | :--- | :--- |
| **Run Flask Server** | `python app_flask.py` | Local development and presentation testing on `http://localhost:5000` |
| **Run Streamlit Server** | `streamlit run app.py` | Presentation testing on `http://localhost:8501` |
| **Train/Fit Model** | `python src/model_training.py` | Recompile `best_model.joblib` after modifying features or logic |
| **Push Hotfix to Vercel** | `git add -A; git commit -m "hotfix"; git push origin main` | Deploy modification live to production URL |

---

> [!TIP]
> Keep this playbook open in your IDE sidebar during the presentation so you can search using `Ctrl+F` and modify the code instantly!
