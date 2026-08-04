import os
import sys
import json
import joblib
import pandas as pd
import numpy as np

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from feature_engineering import add_engineered_features
from preprocessing import REVERSE_CATEGORY_MAP

DIRECTOR_REPUTATION_MAP = {
    "s.s. rajamouli": 9.8, "rajamouli": 9.8, "mani ratnam": 9.6, "christopher nolan": 9.7, 
    "lokesh kanagaraj": 9.4, "shankar": 9.3, "s. shankar": 9.3, "prashanth neel": 9.3, 
    "sukumar": 9.2, "atlee": 9.1, "vetrimaaran": 9.5, "pa. ranjith": 8.9, 
    "nelson dilipkumar": 8.8, "nelson": 8.8, "gautham vasudev menon": 8.7, "gvm": 8.7, 
    "nag ashwin": 9.2, "trivikram srinivas": 8.9, "trivikram": 8.9, "sanjay leela bhansali": 9.1, 
    "rajkumar hirani": 9.5, "rohit shetty": 8.5, "denis villeneuve": 9.4, "james cameron": 9.8, 
    "steven spielberg": 9.6, "quentin tarantino": 9.5, "koratala siva": 8.7, "kartik subbaraj": 9.0,
    "mari selvaraj": 9.1, "lokesh": 9.4, "shankar shanmugam": 9.3
}

PRODUCTION_HOUSE_REPUTATION_MAP = {
    "raaj kamal films international": 9.5, "hombale films": 9.5, "lyca productions": 9.2, 
    "sun pictures": 9.3, "madras talkies": 9.4, "vyjayanthi movies": 9.3, "dvv entertainment": 9.2, 
    "mythri movie makers": 9.1, "yash raj films": 9.3, "marvel studios": 9.4, "geetha arts": 9.0, 
    "red giant movies": 8.8, "sri venkateswara creations": 8.8, "dharma productions": 8.9, 
    "t-series": 8.8, "warner bros": 9.0, "universal pictures": 9.1, "seven screen studio": 8.6, 
    "avm productions": 9.0, "paramount pictures": 8.9, "nadiadwala grandson": 8.5
}

ACTOR_REPUTATION_MAP = {
    "kamal haasan": 9.7, "rajinikanth": 9.8, "vijay": 9.6, "ajith kumar": 9.4, "suriya": 9.3,
    "vikram": 9.2, "dhanush": 9.4, "vijay sethupathi": 9.3, "sivakarthikeyan": 9.0,
    "prabhas": 9.5, "mahesh babu": 9.4, "allu arjun": 9.5, "ram charan": 9.4, "jr ntr": 9.4,
    "yash": 9.4, "rishab shetty": 9.2, "dulquer salmaan": 9.1, "fahadh faasil": 9.5,
    "shah rukh khan": 9.8, "salman khan": 9.4, "aamir khan": 9.6, "hrithik roshan": 9.3,
    "ranbir kapoor": 9.3, "ranveer singh": 9.1
}

ACTRESS_REPUTATION_MAP = {
    "nayanthara": 9.5, "trisha krishnan": 9.2, "samantha ruth prabhu": 9.3, "samantha": 9.3,
    "sai pallavi": 9.4, "rashmika mandanna": 9.2, "mrunal thakur": 9.0, "keerthy suresh": 9.0,
    "deepika padukone": 9.5, "alia bhatt": 9.6, "priyanka chopra": 9.4, "anushka shetty": 9.3,
    "sreeleela": 8.8, "pooja hegde": 8.7, "tamannaah bhatia": 8.8, "triptii dimri": 8.9
}

MUSIC_REPUTATION_MAP = {
    "a.r. rahman": 9.8, "ar rahman": 9.8, "anirudh ravichander": 9.6, "anirudh": 9.6,
    "ilaiyaraaja": 9.7, "m.m. keeravani": 9.5, "santhosh narayanan": 9.2, "harris jayaraj": 9.1,
    "devi sri prasad (dsp)": 9.0, "thaman s": 9.0, "g.v. prakash kumar": 8.9, "yuvan shankar raja": 9.3,
    "hans zimmer": 9.9, "ludwig göransson": 9.6, "pritam": 9.2, "sushin shyam": 9.1
}

class IMDbRatingPredictor:
    def __init__(self, models_dir=None):
        if models_dir is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            models_dir = os.path.join(base_dir, 'models')

        self.model_path = os.path.join(models_dir, 'best_model.joblib')
        self.preprocessor_path = os.path.join(models_dir, 'preprocessor.joblib')
        self.metadata_path = os.path.join(models_dir, 'model_metadata.json')

        if not os.path.exists(self.model_path) or not os.path.exists(self.preprocessor_path):
            raise FileNotFoundError("Model artifacts not found. Please execute src/model_training.py first.")

        self.model = joblib.load(self.model_path)
        self.preprocessor = joblib.load(self.preprocessor_path)

        with open(self.metadata_path, 'r') as f:
            self.metadata = json.load(f)

    def predict_single(self, input_dict):
        """
        Takes raw input metadata dictionary (including Director, Lead Actor/Actress/Co-actors, 
        Music Director, Production House options and automated reputation indices)
        and returns rating category prediction, probabilities, and strategic content recommendations.
        """
        dict_copy = input_dict.copy()

        # Currency and unit conversion
        currency = dict_copy.get('currency', 'INR (₹)')
        unit = dict_copy.get('budget_unit', 'Crores')
        prod_val = float(dict_copy.get('production_budget_val', 15.0))
        mkt_val = float(dict_copy.get('marketing_budget_val', 3.0))

        unit_multipliers = {
            'Crores': 10000000.0,
            'Lakhs': 100000.0,
            'Millions': 1000000.0,
            'Thousands': 1000.0,
            'Full Amount': 1.0
        }
        multiplier = unit_multipliers.get(unit, 10000000.0)

        exchange_rates_to_usd = {
            'INR (₹)': 0.012,
            'USD ($)': 1.0,
            'EUR (€)': 1.08,
            'GBP (£)': 1.28
        }
        rate = exchange_rates_to_usd.get(currency, 0.012)

        total_prod_local = prod_val * multiplier
        total_mkt_local = mkt_val * multiplier

        dict_copy['budget_usd'] = total_prod_local * rate
        dict_copy['marketing_budget_usd'] = total_mkt_local * rate

        # Automated Reputation Index Calculation
        director_name = str(dict_copy.get('director_name', '')).strip().lower()
        banner_name = str(dict_copy.get('production_house', '')).strip().lower()
        actor_name = str(dict_copy.get('lead_actor', '')).strip().lower()
        actress_name = str(dict_copy.get('lead_actress', '')).strip().lower()
        music_name = str(dict_copy.get('music_director', '')).strip().lower()

        director_rep = DIRECTOR_REPUTATION_MAP.get(director_name, float(dict_copy.get('director_score', 7.5)))
        banner_rep = PRODUCTION_HOUSE_REPUTATION_MAP.get(banner_name, 7.5)
        actor_rep = ACTOR_REPUTATION_MAP.get(actor_name, 7.0)
        actress_rep = ACTRESS_REPUTATION_MAP.get(actress_name, 7.0)
        music_rep = MUSIC_REPUTATION_MAP.get(music_name, 7.0)

        pop_tags = dict_copy.get('popularity_tags', [])
        if isinstance(pop_tags, list) and 'A-List Lead Actor Star Power' in pop_tags:
            actor_rep = min(9.9, actor_rep + 0.6)
        if isinstance(pop_tags, list) and 'Hit Music / Soundtrack' in pop_tags:
            music_rep = min(9.9, music_rep + 0.6)
        if isinstance(pop_tags, list) and 'Director Cult Following' in pop_tags:
            director_rep = min(9.9, director_rep + 0.4)

        dict_copy['director_score'] = round(director_rep, 1)
        dict_copy['music_score'] = round(music_rep, 1)
        dict_copy['banner_score'] = round(banner_rep, 1)

        # Composite Cast Score
        avg_star_score = (actor_rep + actress_rep) / 2.0
        dict_copy['cast_score'] = round(min(9.9, max(3.0, avg_star_score)), 1)

        df_input = pd.DataFrame([dict_copy])
        
        # Apply domain feature engineering
        df_featured = add_engineered_features(df_input)
        
        # Transform via preprocessor
        X_transformed = self.preprocessor.transform(df_featured)
        
        # Predict class & probabilities
        pred_class_idx = int(self.model.predict(X_transformed)[0])
        probabilities = self.model.predict_proba(X_transformed)[0]
        
        predicted_category = REVERSE_CATEGORY_MAP[pred_class_idx]
        
        prob_dict = {
            'Low': round(float(probabilities[0]), 4),
            'Medium': round(float(probabilities[1]), 4),
            'High': round(float(probabilities[2]), 4)
        }
        
        recommendation = self._generate_recommendation(predicted_category, prob_dict, dict_copy, currency, unit, prod_val)

        return {
            'predicted_category': predicted_category,
            'confidence': round(float(max(probabilities)) * 100, 2),
            'probabilities': prob_dict,
            'recommendations': recommendation,
            'reputation_indices': {
                'director_index': round(director_rep, 1),
                'actor_index': round(actor_rep, 1),
                'actress_index': round(actress_rep, 1),
                'music_director_index': round(music_rep, 1),
                'production_house_index': round(banner_rep, 1)
            }
        }

    def _generate_recommendation(self, category, probabilities, input_dict, currency, unit, prod_val):
        """
        Generates actionable content insights and marketing strategies for distribution.
        """
        runtime = input_dict.get('runtime_minutes', 140)
        is_short = 1 if runtime < 40 else 0
        curr_symbol = currency.split()[1].replace('(', '').replace(')', '') if '(' in currency else '$'

        if category == 'High':
            tier = "Tier-1 Premium Acquisition"
            marketing_advice = f"Allocate strong pre-release campaign (25-35% of {curr_symbol}{prod_val:.1f} {unit} budget). Highlight lead cast & soundtrack album."
            platform_strategy = "Prime-time digital premiere, Pan-India & Global theatrical release, featured carousel placement."
            action_badge = "Greenlight / Instant Acquisition"
        elif category == 'Medium':
            tier = "Tier-2 Standard Content"
            marketing_advice = f"Targeted digital marketing to genre enthusiasts. Focus on social media promos and music teasers."
            platform_strategy = "Mid-tier placement, catalog bundle inclusion, algorithmic recommendation push."
            action_badge = "Proceed with Standard Budget"
        else:
            tier = "Tier-3 High Risk Content"
            marketing_advice = "Minimize initial marketing spend. Conduct focus group test screenings before wide release."
            platform_strategy = "Niche category listing or ad-supported streaming tier (FAST)."
            action_badge = "Re-evaluate / Re-edit Required"

        return {
            'acquisition_tier': tier,
            'action_badge': action_badge,
            'marketing_strategy': marketing_advice,
            'platform_positioning': platform_strategy,
            'short_film_note': "Optimized for short film festivals & digital short streaming hubs." if is_short else "Standard feature film theatrical & OTT distribution model."
        }

if __name__ == '__main__':
    predictor = IMDbRatingPredictor()
    sample_input = {
        'release_year': 2025,
        'runtime_minutes': 150,
        'primary_genre': 'Action',
        'language': 'Tamil',
        'country': 'India',
        'content_rating': 'UA',
        'currency': 'INR (₹)',
        'budget_unit': 'Crores',
        'production_budget_val': 25.0,
        'marketing_budget_val': 5.0,
        'director_name': 'Mani Ratnam',
        'production_house': 'Madras Talkies',
        'lead_actor': 'Kamal Haasan',
        'lead_actress': 'Trisha Krishnan',
        'co_actors': 'Vijay Sethupathi, Fahadh Faasil',
        'music_director': 'A.R. Rahman',
        'sentiment': 'Dramatic / Intense',
        'content_themes': ['Commercial', 'Action Thriller', 'Biopic'],
        'popularity_tags': ['A-List Lead Actor Star Power', 'Hit Music / Soundtrack', 'Pan-India Release Franchise']
    }
    result = predictor.predict_single(sample_input)
    print("Prediction Result:")
    print(json.dumps(result, indent=2))
