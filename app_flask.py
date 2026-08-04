import os
import sys
import json
import pandas as pd
from flask import Flask, render_template, request, jsonify

# Path setup to resolve src module imports
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, 'src')
MODELS_DIR = os.path.join(BASE_DIR, 'models')
DATASET_PATH = os.path.join(BASE_DIR, 'dataset', 'imdb_movies_dataset.csv')
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from predict import IMDbRatingPredictor

app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)

# Initialize Predictor & Dataset Helper
predictor = None
try:
    predictor = IMDbRatingPredictor(models_dir=MODELS_DIR)
except Exception as e:
    print(f"Warning initializing predictor: {e}")

def load_dataset():
    if os.path.exists(DATASET_PATH):
        return pd.read_csv(DATASET_PATH)
    return None

# Predefined Option Lists
DIRECTORS_LIST = [
    "Lokesh Kanagaraj", "Mani Ratnam", "S.S. Rajamouli", "Christopher Nolan", 
    "S. Shankar", "Prashanth Neel", "Sukumar", "Atlee", "Vetrimaaran", "Pa. Ranjith", 
    "Nelson Dilipkumar", "Gautham Vasudev Menon", "Nag Ashwin", "Trivikram Srinivas", 
    "Sanjay Leela Bhansali", "Rajkumar Hirani", "Rohit Shetty", "Kartik Subbaraj",
    "Mari Selvaraj", "Koratala Siva", "Denis Villeneuve", "Steven Spielberg", 
    "James Cameron", "Quentin Tarantino", "Other / Custom Entry"
]

PRODUCTION_HOUSES_LIST = [
    "Raaj Kamal Films International", "Madras Talkies", "Sun Pictures", "Lyca Productions", 
    "Hombale Films", "Vyjayanthi Movies", "DVV Entertainment", "Mythri Movie Makers", 
    "Geetha Arts", "Red Giant Movies", "Sri Venkateswara Creations", "Seven Screen Studio", 
    "Yash Raj Films", "Dharma Productions", "T-Series", "Nadiadwala Grandson", 
    "Marvel Studios", "Warner Bros", "Universal Pictures", "Paramount Pictures", 
    "AVM Productions", "Other / Custom Entry"
]

ACTORS_LIST = [
    "Kamal Haasan", "Rajinikanth", "Vijay", "Ajith Kumar", "Suriya", "Vikram", 
    "Dhanush", "Vijay Sethupathi", "Sivakarthikeyan", "Karthi", "Jayam Ravi", 
    "Silambarasan TR (STR)", "Arvind Swamy", "Madhavan", "Vishal", "Arya", "Siddharth",
    "Prabhas", "Mahesh Babu", "Allu Arjun", "Ram Charan", "Jr NTR", "Nani", 
    "Vijay Deverakonda", "Pawan Kalyan", "Rana Daggubati", "Ravi Teja", "Naga Chaitanya",
    "Yash", "Rishab Shetty", "Shiva Rajkumar", "Sudeep",
    "Dulquer Salmaan", "Fahadh Faasil", "Prithviraj Sukumaran", "Tovino Thomas", "Mammootty", "Mohanlal",
    "Shah Rukh Khan", "Salman Khan", "Aamir Khan", "Hrithik Roshan", "Ranbir Kapoor", 
    "Ranveer Singh", "Vicky Kaushal", "Ayushmann Khurrana", "Rajkummar Rao", "Shahid Kapoor",
    "Other / Custom Entry"
]

ACTRESSES_LIST = [
    "Trisha Krishnan", "Nayanthara", "Samantha Ruth Prabhu", "Rashmika Mandanna", 
    "Sai Pallavi", "Sreeleela", "Mrunal Thakur", "Keerthy Suresh", "Pooja Hegde", 
    "Tamannaah Bhatia", "Anushka Shetty", "Kajal Aggarwal", "Krithi Shetty", 
    "Kalyani Priyadarshan", "Jyothika", "Andrea Jeremiah", "Nithya Menen", "Aishwarya Rajesh",
    "Deepika Padukone", "Alia Bhatt", "Priyanka Chopra", "Kiara Advani", "Kriti Sanon", 
    "Shraddha Kapoor", "Triptii Dimri", "Janhvi Kapoor", "Ananya Panday", "Wamiqa Gabbi", 
    "Disha Patani", "Katrina Kaif", "Kareena Kapoor", "Tabu",
    "Other / Custom Entry"
]

CO_ACTORS_LIST = [
    "Vijay Sethupathi", "Fahadh Faasil", "Prakash Raj", "SJ Suryah", "Nasser", 
    "Samuthirakani", "Sathyaraj", "Sarathkumar", "Vadivelu", "Yogi Babu", "Soori", 
    "Brahmanandam", "Vennela Kishore", "Sunil", "Jagapathi Babu", "Rao Ramesh", 
    "Bobby Simha", "Pasupathy", "Kalabhavan Shajohn", "Paresh Rawal", 
    "Nawazuddin Siddiqui", "Pankaj Tripathi", "Manoj Bajpayee", "Boman Irani"
]

MUSIC_DIRECTORS_LIST = [
    "Anirudh Ravichander", "A.R. Rahman", "Ilaiyaraaja", "M.M. Keeravani", 
    "Santhosh Narayanan", "Devi Sri Prasad (DSP)", "Thaman S", "G.V. Prakash Kumar", 
    "Harris Jayaraj", "Yuvan Shankar Raja", "Sam C.S.", "Ghibran", "Sean Roldan", 
    "Sushin Shyam", "Jakes Bejoy", "Hesham Abdul Wahab", "D. Imman", "Nivas K. Prasanna",
    "Pritam", "Vishal-Shekhar", "Amit Trivedi", "Sachin-Jigar", "Ajay-Atul",
    "Hans Zimmer", "Ludwig Göransson", "Howard Shore", "John Williams",
    "Other / Custom Entry"
]

THEMES_50_PLUS = [
    'Action Thriller', 'Commercial Mass Entertainer', 'Women-Centric / Female Lead', 'Biopic & Historical Figure', 
    'Life Story & True Events', 'Tech / Cyberpunk / Sci-Fi', 'Festival & Art House Indie', 'Family Drama & Relations', 
    'Mythological & Epic Fantasy', 'Psychological Thriller', 'Crime & Mafia Syndicate', 'Underdog & Sports Triumph', 
    'Romantic Comedy (Rom-Com)', 'Social Justice & Political Commentary', 'Survival & Natural Disaster', 'Supernatural & Horror Mystery', 
    'Space Exploration & Sci-Fi Odyssey', 'Coming of Age & Youth', 'Philosophical & Existential', 'Police Procedural & Investigation', 
    'Revenge & Vigilante Action', 'Military & Patriotic War', 'Time Travel & Multiverse', 'Courtroom & Legal Drama', 
    'High School & Campus Drama', 'Musical & Performing Arts', 'Black Comedy & Satire', 'Heist & Con Artist', 
    'Spy & Secret Agent Thriller', 'Environmental & Ecological', 'Gangster & Underworld Saga', 'Post-Apocalyptic & Dystopian', 
    'Road Trip & Journey', 'Tragedy & Dark Drama', 'Small Town & Rural Realism', 'Neo-Noir & Mystery Detective', 
    'Medical & Hospital Drama', 'Corporate Thriller & Business', 'Parent-Child Relationship', 'Friendship & Brotherhood', 
    'Period Drama & Vintage Era', 'Martial Arts & Fighting Action', 'Zombie & Monster Creature', 'Animation & Superhero Origin', 
    'Philosophical Thriller', 'Slasher & Gore Horror', 'Submarine & Naval Warfare', 'Cyber Crime & Ethical Hacking', 
    'Religious & Folk Lore Legend', 'Docudrama & Investigative Journalism', 'Multilingual Pan-India Spectacle', 'Short-Form Experimental Short'
]

POPULARITY_TAGS_LIST = [
    'A-List Lead Actor Star Power', 
    'Hit Music / Soundtrack', 
    'Pan-India Release Franchise', 
    'Viral Teaser / Social Hype', 
    'National Award / Festival Acclaim', 
    'Director Cult Following'
]

# Route 1: Landing Page
@app.route('/')
def landing_page():
    return render_template('index.html')

# Route 2: Prediction Application Page
@app.route('/app')
def application_page():
    options_data = {
        'directors': DIRECTORS_LIST,
        'banners': PRODUCTION_HOUSES_LIST,
        'actors': ACTORS_LIST,
        'actresses': ACTRESSES_LIST,
        'co_actors': CO_ACTORS_LIST,
        'music_directors': MUSIC_DIRECTORS_LIST,
        'themes': THEMES_50_PLUS,
        'popularity_tags': POPULARITY_TAGS_LIST
    }
    return render_template('app.html', options=options_data)

# Route 3: Dedicated About Page with Model Benchmarks, EDA, & Architecture
@app.route('/about')
def about_page():
    global predictor
    if predictor is None:
        try:
            predictor = IMDbRatingPredictor(models_dir=MODELS_DIR)
        except Exception:
            pass

    metadata = predictor.metadata if predictor else {}
    df_data = load_dataset()
    sample_records = df_data.head(15).to_dict(orient='records') if df_data is not None else []
    
    return render_template('about.html', metadata=metadata, dataset_sample=sample_records)

# REST API Endpoint: Predict
@app.route('/api/predict', methods=['POST'])
def api_predict():
    global predictor
    if predictor is None:
        try:
            predictor = IMDbRatingPredictor(models_dir=MODELS_DIR)
        except Exception as e:
            return jsonify({'status': 'error', 'message': f'Predictor initialization failed: {str(e)}'}), 500

    try:
        data = request.get_json(force=True)
        result = predictor.predict_single(data)
        return jsonify({'status': 'success', 'data': result})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
