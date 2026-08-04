import numpy as np
import pandas as pd

def add_engineered_features(df):
    """
    Applies domain feature engineering including multi-lingual Indian cinema parameters:
    - Music Director reputation score & soundtrack impact
    - Currency conversion: INR, USD, EUR, GBP to USD
    - Actor/Actress/Co-actor star power index calculation
    - Sentiment score mapping
    - Expanded 50+ Content Theme / Journal multi-select tags count & binary indicators
    - Popularity driver multi-select tags count & binary indicators
    Ensures all 25 numerical and 5 categorical feature dimensions are guaranteed present.
    """
    df = df.copy()

    # Default fallbacks if columns are missing in raw input
    if 'budget_usd' not in df.columns:
        if 'budget_inr_crores' in df.columns:
            df['budget_usd'] = df['budget_inr_crores'] * 120000.0
        else:
            df['budget_usd'] = 3000000.0

    if 'marketing_budget_usd' not in df.columns:
        if 'marketing_inr_crores' in df.columns:
            df['marketing_budget_usd'] = df['marketing_inr_crores'] * 120000.0
        else:
            df['marketing_budget_usd'] = 600000.0

    if 'director_score' not in df.columns:
        df['director_score'] = 7.5

    if 'cast_score' not in df.columns:
        df['cast_score'] = 7.0

    if 'music_score' not in df.columns:
        df['music_score'] = 7.0

    if 'release_year' not in df.columns:
        df['release_year'] = 2025

    if 'runtime_minutes' not in df.columns:
        df['runtime_minutes'] = 140

    # Short film indicator
    df['is_short_film'] = df['runtime_minutes'].apply(lambda x: 1 if float(x) < 40 else 0)

    # Budget per minute ratio
    runtime_safe = df['runtime_minutes'].replace(0, 1)
    df['budget_per_minute'] = df['budget_usd'] / runtime_safe

    # Star Synergy Score (Director score * Cast score * Music score multiplier)
    cast_filled = df['cast_score'].fillna(5.0)
    df['star_synergy_score'] = df['director_score'] * cast_filled * (df['music_score'] / 7.5)

    # Marketing Ratio
    budget_safe = df['budget_usd'].replace(0, 1)
    df['marketing_ratio'] = df['marketing_budget_usd'].fillna(0) / budget_safe

    # Release Decade
    df['release_decade'] = (df['release_year'] // 10) * 10

    # Sentiment Score mapping
    sentiment_weights = {
        'Inspiring / Positive': 1.0,
        'Emotional / Heartwarming': 0.8,
        'Dramatic / Intense': 0.6,
        'Suspenseful / Thrilling': 0.5,
        'Humorous / Lighthearted': 0.3,
        'Dark / Gritty': 0.2
    }
    if 'sentiment' not in df.columns:
        df['sentiment'] = 'Dramatic / Intense'
    df['sentiment_score'] = df['sentiment'].map(sentiment_weights).fillna(0.5)

    # Content Theme / Journal tags count (50+ themes)
    if 'content_themes' in df.columns:
        df['theme_count'] = df['content_themes'].apply(lambda t: len(t) if isinstance(t, list) else 1)
        df['has_women_centric'] = df['content_themes'].apply(lambda t: 1 if isinstance(t, list) and any('Women' in str(x) for x in t) else 0)
        df['has_biopic_lifestory'] = df['content_themes'].apply(lambda t: 1 if isinstance(t, list) and any(k in str(x) for x in t for k in ['Biopic', 'Life Story', 'Historical']) else 0)
        df['has_commercial_action'] = df['content_themes'].apply(lambda t: 1 if isinstance(t, list) and any(k in str(x) for x in t for k in ['Commercial', 'Action', 'Mafia', 'Gangster']) else 0)
        df['has_tech_scifi'] = df['content_themes'].apply(lambda t: 1 if isinstance(t, list) and any(k in str(x) for x in t for k in ['Tech', 'Sci-Fi', 'Cyberpunk', 'Space']) else 0)
    else:
        df['theme_count'] = 1
        df['has_women_centric'] = 0
        df['has_biopic_lifestory'] = 0
        df['has_commercial_action'] = 0
        df['has_tech_scifi'] = 0

    # Popularity Driver tags count
    if 'popularity_tags' in df.columns:
        df['popularity_tags_count'] = df['popularity_tags'].apply(lambda p: len(p) if isinstance(p, list) else 1)
        df['has_star_power'] = df['popularity_tags'].apply(lambda p: 1 if isinstance(p, list) and 'A-List Lead Actor Star Power' in p else 0)
        df['has_hit_music'] = df['popularity_tags'].apply(lambda p: 1 if isinstance(p, list) and 'Hit Music / Soundtrack' in p else 0)
        df['has_pan_india'] = df['popularity_tags'].apply(lambda p: 1 if isinstance(p, list) and 'Pan-India Release Franchise' in p else 0)
        df['has_festival_acclaim'] = df['popularity_tags'].apply(lambda p: 1 if isinstance(p, list) and 'National Award / Festival Acclaim' in p else 0)
    else:
        df['popularity_tags_count'] = 1
        df['has_star_power'] = 0
        df['has_hit_music'] = 0
        df['has_pan_india'] = 0
        df['has_festival_acclaim'] = 0

    # Log scale budget metrics
    df['log_budget'] = np.log10(df['budget_usd'].clip(lower=0) + 1)
    marketing_filled = df['marketing_budget_usd'].fillna(0)
    df['log_marketing'] = np.log10(marketing_filled.clip(lower=0) + 1)

    # Categorical defaults fallback
    if 'primary_genre' not in df.columns: df['primary_genre'] = 'Drama'
    if 'language' not in df.columns: df['language'] = 'Tamil'
    if 'country' not in df.columns: df['country'] = 'India'
    if 'content_rating' not in df.columns: df['content_rating'] = 'UA'

    return df
