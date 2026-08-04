import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

CATEGORICAL_FEATURES = ['primary_genre', 'language', 'country', 'content_rating', 'sentiment']
NUMERICAL_FEATURES = [
    'release_year', 'runtime_minutes', 'is_short_film', 
    'budget_usd', 'marketing_budget_usd', 'director_score', 
    'cast_score', 'music_score', 'budget_per_minute', 'star_synergy_score', 
    'marketing_ratio', 'release_decade', 'log_budget', 'log_marketing',
    'sentiment_score', 'theme_count', 'has_women_centric', 'has_biopic_lifestory',
    'has_commercial_action', 'has_tech_scifi', 'popularity_tags_count',
    'has_star_power', 'has_hit_music', 'has_pan_india', 'has_festival_acclaim'
]
TARGET_COL = 'rating_category'

# Label mapping for categories
CATEGORY_MAP = {'Low': 0, 'Medium': 1, 'High': 2}
REVERSE_CATEGORY_MAP = {0: 'Low', 1: 'Medium', 2: 'High'}

def build_preprocessing_pipeline(cat_features=CATEGORICAL_FEATURES, num_features=NUMERICAL_FEATURES):
    """
    Constructs ColumnTransformer pipeline with numerical imputer + scaler
    and categorical imputer + One-Hot encoder.
    """
    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    cat_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', num_pipeline, num_features),
            ('cat', cat_pipeline, cat_features)
        ]
    )
    
    return preprocessor

def prepare_data(df, test_size=0.2, random_state=42):
    """
    Splits raw dataset into train and test sets, then fits preprocessor strictly on train set.
    """
    df = df.copy()
    
    if TARGET_COL not in df.columns:
        raise ValueError(f"Target column '{TARGET_COL}' missing from dataset.")
    
    y = df[TARGET_COL].map(CATEGORY_MAP)
    
    # Drop non-feature identifiers
    drop_cols = [
        TARGET_COL, 'imdb_score', 'movie_id', 'title', 'lead_actor', 
        'lead_actress', 'co_actors', 'music_director', 'content_themes', 'popularity_tags'
    ]
    X = df.drop(columns=[c for c in drop_cols if c in df.columns], errors='ignore')
    
    # Train-test split FIRST to avoid data leakage
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    cat_cols = [c for c in CATEGORICAL_FEATURES if c in X.columns]
    num_cols = [n for n in NUMERICAL_FEATURES if n in X.columns]
    
    preprocessor = build_preprocessing_pipeline(cat_features=cat_cols, num_features=num_cols)
    
    X_train_transformed = preprocessor.fit_transform(X_train)
    X_test_transformed = preprocessor.transform(X_test)
    
    cat_encoder = preprocessor.named_transformers_['cat'].named_steps['onehot']
    encoded_cat_names = cat_encoder.get_feature_names_out(cat_cols).tolist()
    feature_names = num_cols + encoded_cat_names
    
    return {
        'X_train': X_train_transformed,
        'X_test': X_test_transformed,
        'y_train': y_train.values,
        'y_test': y_test.values,
        'preprocessor': preprocessor,
        'feature_names': feature_names,
        'num_cols': num_cols,
        'cat_cols': cat_cols,
        'X_train_raw': X_train,
        'X_test_raw': X_test
    }
