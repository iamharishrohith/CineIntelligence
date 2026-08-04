import os
import sys
import json
import joblib
import numpy as np
import pandas as pd

# Ensure src directory is in sys.path for seamless imports
SRC_DIR = os.path.dirname(os.path.abspath(__file__))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score
)

from data_loader import load_data
from feature_engineering import add_engineered_features
from preprocessing import prepare_data, REVERSE_CATEGORY_MAP

def train_and_evaluate_models():
    """
    Trains multiple ML classification models for IMDb Rating Category Prediction.
    Evaluates each model using multi-class metrics (Accuracy, Precision, Recall, F1, ROC-AUC).
    Selects the best model and serializes all artifacts into models/ directory.
    """
    print("Step 1: Loading raw dataset...")
    df_raw = load_data()
    
    print("Step 2: Performing feature engineering...")
    df_featured = add_engineered_features(df_raw)
    
    print("Step 3: Preprocessing data with strict train/test split...")
    data_dict = prepare_data(df_featured, test_size=0.2, random_state=42)
    
    X_train = data_dict['X_train']
    X_test = data_dict['X_test']
    y_train = data_dict['y_train']
    y_test = data_dict['y_test']
    preprocessor = data_dict['preprocessor']
    feature_names = data_dict['feature_names']
    
    print(f"Data shapes -> X_train: {X_train.shape}, X_test: {X_test.shape}")

    # Define candidate models
    candidate_models = {
        'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42, C=1.0),
        'Random Forest': RandomForestClassifier(n_estimators=150, max_depth=12, random_state=42, class_weight='balanced'),
        'Gradient Boosting': GradientBoostingClassifier(n_estimators=120, learning_rate=0.08, max_depth=5, random_state=42)
    }

    results = {}
    best_model_name = None
    best_f1 = -1.0
    best_model_obj = None

    print("\nStep 4: Training & Evaluating Machine Learning Models...")
    print("=" * 70)

    for name, model in candidate_models.items():
        # Train model
        model.fit(X_train, y_train)
        
        # Predictions
        y_pred = model.predict(X_test)
        y_proba = model.predict_proba(X_test) if hasattr(model, "predict_proba") else None
        
        # Compute metrics
        acc = float(accuracy_score(y_test, y_pred))
        prec = float(precision_score(y_test, y_pred, average='weighted', zero_division=0))
        rec = float(recall_score(y_test, y_pred, average='weighted', zero_division=0))
        f1 = float(f1_score(y_test, y_pred, average='weighted', zero_division=0))
        cm = confusion_matrix(y_test, y_pred).tolist()
        
        # ROC-AUC (multi-class One-vs-Rest)
        try:
            roc_auc = float(roc_auc_score(y_test, y_proba, multi_class='ovr', average='weighted'))
        except Exception:
            roc_auc = 0.0

        results[name] = {
            'accuracy': round(acc, 4),
            'precision': round(prec, 4),
            'recall': round(rec, 4),
            'f1_score': round(f1, 4),
            'roc_auc': round(roc_auc, 4),
            'confusion_matrix': cm,
            'classification_report': classification_report(
                y_test, y_pred, target_names=['Low', 'Medium', 'High'], output_dict=True
            )
        }

        print(f"[{name}]")
        print(f"  Accuracy  : {acc:.4f}")
        print(f"  Precision : {prec:.4f}")
        print(f"  Recall    : {rec:.4f}")
        print(f"  F1 Score  : {f1:.4f}")
        print(f"  ROC-AUC   : {roc_auc:.4f}")
        print("-" * 70)

        if f1 > best_f1:
            best_f1 = f1
            best_model_name = name
            best_model_obj = model

    print(f"\nOptimal Selected Model: {best_model_name} (F1 Score: {best_f1:.4f})")

    # Step 5: Save Model Artifacts
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    models_dir = os.path.join(base_dir, 'models')
    os.makedirs(models_dir, exist_ok=True)

    # 1. Best model file
    model_path = os.path.join(models_dir, 'best_model.joblib')
    joblib.dump(best_model_obj, model_path)
    
    # 2. Preprocessor pipeline file
    preprocessor_path = os.path.join(models_dir, 'preprocessor.joblib')
    joblib.dump(preprocessor, preprocessor_path)

    # 3. Metadata & Feature names JSON
    feature_importance_dict = {}
    if hasattr(best_model_obj, 'feature_importances_'):
        importances = best_model_obj.feature_importances_
        # Sort top features
        top_idx = np.argsort(importances)[::-1]
        feature_importance_dict = {feature_names[i]: round(float(importances[i]), 5) for i in top_idx}

    metadata = {
        'best_model_name': best_model_name,
        'feature_names': feature_names,
        'num_cols': data_dict['num_cols'],
        'cat_cols': data_dict['cat_cols'],
        'feature_importances': feature_importance_dict,
        'evaluation_results': results
    }

    metadata_path = os.path.join(models_dir, 'model_metadata.json')
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=4)

    print(f"\nArtifacts saved successfully in '{os.path.abspath(models_dir)}':")
    print(f" - Best Model    : {model_path}")
    print(f" - Preprocessor  : {preprocessor_path}")
    print(f" - Metadata      : {metadata_path}")
    
    return results, best_model_name

if __name__ == '__main__':
    train_and_evaluate_models()
