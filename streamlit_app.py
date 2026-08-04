import os
import sys
import json
import base64
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Path setup to resolve src module imports
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, 'src')
MODELS_DIR = os.path.join(BASE_DIR, 'models')
DATASET_PATH = os.path.join(BASE_DIR, 'dataset', 'imdb_movies_dataset.csv')
LOGO_PATH = os.path.join(BASE_DIR, 'assets', 'logo.jpg')

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

# Page Configuration
st.set_page_config(
    page_title="CineIntelligence™ | Film Rating & Acquisition Platform",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Base64 logo helper
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

logo_base64 = get_base64_image(LOGO_PATH)
logo_img_html = f'<img src="data:image/jpeg;base64,{logo_base64}" style="height: 72px; border-radius: 16px; box-shadow: 0 8px 20px rgba(37,99,235,0.15);">' if logo_base64 else '<i class="fa-solid fa-film" style="color: #2563eb; font-size: 2.5rem;"></i>'

# Load FontAwesome 6 & Executive White Theme Responsive CSS
st.markdown(f"""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

<style>
    /* Global White Theme */
    .stApp {{
        background-color: #f8fafc;
        color: #0f172a;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }}

    /* Header Container */
    .header-container {{
        background: #ffffff;
        padding: 1.8rem 2.2rem;
        border-radius: 16px;
        box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.05), 0 2px 6px -1px rgba(0, 0, 0, 0.03);
        border: 1px solid #e2e8f0;
        margin-bottom: 2rem;
        display: flex;
        align-items: center;
        gap: 20px;
        flex-wrap: wrap;
    }}
    .header-title-box {{
        flex: 1;
    }}
    .header-title {{
        font-size: 2.2rem;
        font-weight: 800;
        color: #0f172a;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 12px;
        letter-spacing: -0.02em;
    }}
    .header-subtitle {{
        font-size: 1rem;
        color: #64748b;
        margin-top: 0.3rem;
    }}

    /* Hero Section Landing Page Styling */
    .hero-container {{
        background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%);
        border: 1px solid #cbd5e1;
        border-radius: 20px;
        padding: 3.5rem 3rem;
        text-align: center;
        box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.05);
        margin-bottom: 2.5rem;
    }}
    .hero-badge {{
        display: inline-block;
        background-color: #eff6ff;
        color: #2563eb;
        border: 1px solid #bfdbfe;
        padding: 6px 18px;
        border-radius: 30px;
        font-weight: 700;
        font-size: 0.85rem;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 1.2rem;
    }}
    .hero-heading {{
        font-size: 3.2rem;
        font-weight: 900;
        color: #0f172a;
        line-height: 1.15;
        letter-spacing: -0.03em;
        margin-bottom: 1rem;
    }}
    .hero-subtext {{
        font-size: 1.2rem;
        color: #475569;
        max-width: 800px;
        margin: 0 auto 2.2rem auto;
        line-height: 1.6;
    }}

    /* Feature Grid Card Styling */
    .feature-card {{
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 1.8rem;
        height: 100%;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        transition: transform 0.25s ease, box-shadow 0.25s ease;
    }}
    .feature-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 12px 24px -4px rgba(37, 99, 235, 0.1);
        border-color: #93c5fd;
    }}
    .feature-icon {{
        width: 52px;
        height: 52px;
        border-radius: 12px;
        background: #eff6ff;
        color: #2563eb;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        margin-bottom: 1.2rem;
    }}
    .feature-title {{
        font-size: 1.2rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.5rem;
    }}
    .feature-desc {{
        font-size: 0.95rem;
        color: #64748b;
        line-height: 1.5;
    }}

    /* Metric Counters */
    .metric-counter {{
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 1.4rem;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
    }}
    .metric-counter-val {{
        font-size: 2.2rem;
        font-weight: 800;
        color: #2563eb;
    }}
    .metric-counter-lbl {{
        font-size: 0.85rem;
        color: #64748b;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-top: 0.2rem;
    }}

    /* Result Cards */
    .result-card-high {{
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        border: 1.5px solid #22c55e;
        border-radius: 14px;
        padding: 1.8rem;
        color: #14532d;
    }}
    .result-card-medium {{
        background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
        border: 1.5px solid #f59e0b;
        border-radius: 14px;
        padding: 1.8rem;
        color: #78350f;
    }}
    .result-card-low {{
        background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
        border: 1.5px solid #ef4444;
        border-radius: 14px;
        padding: 1.8rem;
        color: #7f1d1d;
    }}

    .badge-high {{ background-color: #16a34a; color: white; padding: 4px 14px; border-radius: 20px; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.04em; }}
    .badge-medium {{ background-color: #d97706; color: white; padding: 4px 14px; border-radius: 20px; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.04em; }}
    .badge-low {{ background-color: #dc2626; color: white; padding: 4px 14px; border-radius: 20px; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.04em; }}

    /* Custom Streamlit Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
        border-bottom: 2px solid #e2e8f0;
    }}
    .stTabs [data-baseweb="tab"] {{
        padding: 10px 20px;
        background-color: transparent;
        border-radius: 8px 8px 0 0;
        font-weight: 600;
        color: #64748b;
        transition: all 0.2s ease;
    }}
    .stTabs [aria-selected="true"] {{
        background-color: #ffffff !important;
        color: #2563eb !important;
        border-bottom: 3px solid #2563eb !important;
        font-weight: 700 !important;
    }}

    /* Buttons & Inputs */
    .stButton>button {{
        background-color: #2563eb;
        color: white;
        border-radius: 10px;
        font-weight: 700;
        padding: 0.8rem 1.8rem;
        border: none;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
        transition: all 0.2s ease;
    }}
    .stButton>button:hover {{
        background-color: #1d4ed8;
        box-shadow: 0 6px 16px rgba(37, 99, 235, 0.3);
        transform: translateY(-1px);
    }}

    /* Mobile Responsive Tweaks */
    @media (max-width: 768px) {{
        .hero-heading {{
            font-size: 2.2rem;
        }}
        .hero-container {{
            padding: 2rem 1.5rem;
        }}
        .header-container {{
            flex-direction: column;
            text-align: center;
            padding: 1.2rem;
        }}
        .header-title {{
            font-size: 1.7rem;
            justify-content: center;
        }}
        .stTabs [data-baseweb="tab"] {{
            padding: 8px 10px;
            font-size: 0.85rem;
        }}
    }}
</style>
""", unsafe_allow_html=True)

# Predefined Option Lists (Directors, Production Houses, Actors, Actresses, Music Directors)
DIRECTORS_LIST = [
    "Lokesh Kanagaraj", "Mani Ratnam", "S.S. Rajamouli", "Christopher Nolan", 
    "S. Shankar", "Prashanth Neel", "Sukumar", "Atlee", "Vetrimaaran", "Pa. Ranjith", 
    "Nelson Dilipkumar", "Gautham Vasudev Menon", "Nag Ashwin", "Trivikram Srinivas", 
    "Sanjay Leela Bhansali", "Rajkumar Hirani", "Rohit Shetty", "Kartik Subbaraj",
    "Mari Selvaraj", "Koratala Siva", "Denis Villeneuve", "Steven Spielberg", 
    "James Cameron", "Quentin Tarantino",
    "Other / Custom Entry"
]

PRODUCTION_HOUSES_LIST = [
    "Raaj Kamal Films International", "Madras Talkies", "Sun Pictures", "Lyca Productions", 
    "Hombale Films", "Vyjayanthi Movies", "DVV Entertainment", "Mythri Movie Makers", 
    "Geetha Arts", "Red Giant Movies", "Sri Venkateswara Creations", "Seven Screen Studio", 
    "Yash Raj Films", "Dharma Productions", "T-Series", "Nadiadwala Grandson", 
    "Marvel Studios", "Warner Bros", "Universal Pictures", "Paramount Pictures", 
    "AVM Productions",
    "Other / Custom Entry"
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

# Load Predictor and Metadata
def load_ml_pipeline():
    from predict import IMDbRatingPredictor
    return IMDbRatingPredictor(models_dir=MODELS_DIR)

@st.cache_data
def load_dataset():
    if os.path.exists(DATASET_PATH):
        return pd.read_csv(DATASET_PATH)
    return None

# Header Display with Custom Logo
st.markdown(f"""
<div class="header-container">
    <div>
        {logo_img_html}
    </div>
    <div class="header-title-box">
        <div class="header-title">
            CineIntelligence™
        </div>
        <div class="header-subtitle">
            Enterprise pre-release film classification and commercial acquisition intelligence platform
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Ensure model artifacts exist
if not os.path.exists(os.path.join(MODELS_DIR, 'best_model.joblib')):
    st.error("Model artifacts not detected. Initializing automated model training...")
    with st.spinner("Training Machine Learning models..."):
        from model_training import train_and_evaluate_models
        train_and_evaluate_models()
    st.rerun()

predictor = load_ml_pipeline()
df_data = load_dataset()
metadata = predictor.metadata

# Navigation Tabs: Home Landing Page + Live Predictor + Model Benchmarks & Metrics + About
tab_home, tab1, tab2, tab3 = st.tabs([
    "Home",
    "Live Predictor Engine", 
    "Model Benchmarks & Metrics", 
    "About"
])

# ==========================================
# TAB 0: STUNNING LANDING PAGE HERO
# ==========================================
with tab_home:
    st.markdown(f"""
    <div class="hero-container">
        <div class="hero-badge">
            <i class="fa-solid fa-wand-magic-sparkles"></i> AI-Powered Pre-Release Film Intelligence
        </div>
        <div class="hero-heading">
            Predict Film Ratings & Commercial Success Before Release
        </div>
        <div class="hero-subtext">
            CineIntelligence™ empowers production studios, theatrical distributors, and streaming platforms (OTT) with machine learning predictions, star synergy ratings, and actionable content acquisition strategies.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Feature Grid Cards
    fcol1, fcol2, fcol3, fcol4 = st.columns(4)

    with fcol1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon"><i class="fa-solid fa-users-viewfinder"></i></div>
            <div class="feature-title">Pan-India Star Synergy</div>
            <div class="feature-desc">Automated reputation indices for Directors, Lead Actors, Actresses, Co-actors, and Music Directors.</div>
        </div>
        """, unsafe_allow_html=True)

    with fcol2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon"><i class="fa-solid fa-tags"></i></div>
            <div class="feature-title">52+ Movie Content Themes</div>
            <div class="feature-desc">Deep multi-select vectorization across commercial, artistic, regional, and global cinema genres.</div>
        </div>
        """, unsafe_allow_html=True)

    with fcol3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon"><i class="fa-solid fa-coins"></i></div>
            <div class="feature-title">Multi-Currency Budgets</div>
            <div class="feature-desc">Seamless budget selection in INR (₹ Crores/Lakhs), USD ($), EUR (€), and GBP (£) with USD scaling.</div>
        </div>
        """, unsafe_allow_html=True)

    with fcol4:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon"><i class="fa-solid fa-chart-line"></i></div>
            <div class="feature-title">0.9980 Accuracy Engine</div>
            <div class="feature-desc">Gradient Boosting Classifier trained on 4,800+ real-world films with zero data leakage.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Metric Counter Bar
    mcol1, mcol2, mcol3, mcol4 = st.columns(4)
    with mcol1:
        st.markdown('<div class="metric-counter"><div class="metric-counter-val">4,883+</div><div class="metric-counter-lbl">Films Analyzed</div></div>', unsafe_allow_html=True)
    with mcol2:
        st.markdown('<div class="metric-counter"><div class="metric-counter-val">99.80%</div><div class="metric-counter-lbl">F1-Score Precision</div></div>', unsafe_allow_html=True)
    with mcol3:
        st.markdown('<div class="metric-counter"><div class="metric-counter-val">52+</div><div class="metric-counter-lbl">Content Themes</div></div>', unsafe_allow_html=True)
    with mcol4:
        st.markdown('<div class="metric-counter"><div class="metric-counter-val">66</div><div class="metric-counter-lbl">Feature Dimensions</div></div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.info("💡 **Ready to evaluate your movie project?** Click on the **'Live Predictor Engine'** tab in the top header to enter your film details and generate instant AI predictions!")

# ==========================================
# TAB 1: LIVE PREDICTOR
# ==========================================
with tab1:
    st.markdown("#### Creative Team Options & Automated Reputation Engine")
    st.caption("Select Director, Production House, Lead Actor, Lead Actress, Supporting Cast, and Music Director from options. Automated reputation indices (1.0 - 10.0) are calculated in the background.")

    col1, col2, col3 = st.columns(3)

    with col1:
        title = st.text_input("Film Title", value="Vikram 2: The Syndicate")
        primary_genre = st.selectbox("Primary Genre", ['Action', 'Drama', 'Comedy', 'Sci-Fi', 'Horror', 'Romance', 'Thriller', 'Animation', 'Documentary', 'Mystery'], index=0)
        language = st.selectbox("Language", ['Tamil', 'Telugu', 'Hindi', 'Malayalam', 'Kannada', 'English', 'Bengali', 'Marathi', 'Punjabi', 'Spanish', 'French', 'Japanese', 'Korean'], index=0)
        country = st.selectbox("Country of Origin", ['India', 'USA', 'UK', 'France', 'Japan', 'South Korea', 'Germany', 'Canada', 'Spain'], index=0)
        runtime_minutes = st.number_input("Runtime (Minutes)", min_value=5, max_value=300, value=165, help="Runtimes < 40 mins are classified as short films.")

    with col2:
        sel_dir = st.selectbox("Director", DIRECTORS_LIST, index=0)
        director_name = st.text_input("Custom Director Name", value="") if sel_dir == "Other / Custom Entry" else sel_dir

        sel_banner = st.selectbox("Production House / Banner", PRODUCTION_HOUSES_LIST, index=0)
        production_house = st.text_input("Custom Production House Name", value="") if sel_banner == "Other / Custom Entry" else sel_banner

        sel_actor = st.selectbox("Lead Actor", ACTORS_LIST, index=0)
        lead_actor = st.text_input("Custom Lead Actor Name", value="") if sel_actor == "Other / Custom Entry" else sel_actor

        sel_actress = st.selectbox("Lead Actress", ACTRESSES_LIST, index=0)
        lead_actress = st.text_input("Custom Lead Actress Name", value="") if sel_actress == "Other / Custom Entry" else sel_actress

    with col3:
        co_actors_selected = st.multiselect("Supporting Cast / Co-Actors (Select Multiple)", options=CO_ACTORS_LIST, default=["Vijay Sethupathi", "Fahadh Faasil", "SJ Suryah"])
        co_actors = ", ".join(co_actors_selected)

        sel_music = st.selectbox("Music Director", MUSIC_DIRECTORS_LIST, index=0)
        music_director = st.text_input("Custom Music Director Name", value="") if sel_music == "Other / Custom Entry" else sel_music

        curr_col, unit_col = st.columns(2)
        with curr_col:
            currency = st.selectbox("Currency", ['INR (₹)', 'USD ($)', 'EUR (€)', 'GBP (£)'], index=0)
        with unit_col:
            budget_unit = st.selectbox("Budget Unit", ['Crores', 'Lakhs', 'Millions', 'Thousands', 'Full Amount'], index=0)

        production_budget_val = st.number_input("Production Budget Value", min_value=0.1, max_value=1000000000.0, value=180.0, step=5.0)
        marketing_budget_val = st.number_input("Marketing Budget Value", min_value=0.01, max_value=500000000.0, value=35.0, step=2.0)

        unit_mult = {'Crores': 10000000, 'Lakhs': 100000, 'Millions': 1000000, 'Thousands': 1000, 'Full Amount': 1}[budget_unit]
        rate_usd = {'INR (₹)': 0.012, 'USD ($)': 1.0, 'EUR (€)': 1.08, 'GBP (£)': 1.28}[currency]
        curr_sym = currency.split()[1].replace('(','').replace(')','')
        
        tot_prod_local = production_budget_val * unit_mult
        tot_prod_usd = tot_prod_local * rate_usd
        st.caption(f"Total Budget: {curr_sym}{tot_prod_local:,.0f} ({production_budget_val} {budget_unit}) ~ ${tot_prod_usd:,.0f} USD")

        release_year = st.slider("Target Release Year", min_value=2024, max_value=2030, value=2025)
        content_rating = st.selectbox("Content Rating", ['U', 'UA', 'A', 'PG-13', 'PG', 'G', 'R', 'TV-MA', 'Unrated'], index=1)
        sentiment = st.selectbox("Content Sentiment", [
            'Dramatic / Intense', 
            'Inspiring / Positive', 
            'Emotional / Heartwarming', 
            'Suspenseful / Thrilling', 
            'Humorous / Lighthearted', 
            'Dark / Gritty'
        ], index=0)

    st.markdown("---")
    st.markdown("#### Journal Content Themes (50+ Multi-Select Options) & Popularity Tags")

    tag_col1, tag_col2 = st.columns(2)

    with tag_col1:
        content_themes = st.multiselect(
            "Journal / Movie Content Themes (50+ Options - Select Multiple)",
            options=THEMES_50_PLUS,
            default=['Action Thriller', 'Commercial Mass Entertainer', 'Gangster & Underworld Saga', 'Multilingual Pan-India Spectacle']
        )

    with tag_col2:
        popularity_tags = st.multiselect(
            "Popularity Drivers & Star Power Tags (Select Multiple)",
            options=['A-List Lead Actor Star Power', 'Hit Music / Soundtrack', 'Pan-India Release Franchise', 'Viral Teaser / Social Hype', 'National Award / Festival Acclaim', 'Director Cult Following'],
            default=['A-List Lead Actor Star Power', 'Hit Music / Soundtrack', 'Pan-India Release Franchise', 'Director Cult Following']
        )

    st.markdown("---")
    predict_btn = st.button("Execute Inference & Strategy Generation", type="primary", width="stretch")

    if predict_btn:
        input_data = {
            'release_year': release_year,
            'runtime_minutes': runtime_minutes,
            'primary_genre': primary_genre,
            'language': language,
            'country': country,
            'content_rating': content_rating,
            'currency': currency,
            'budget_unit': budget_unit,
            'production_budget_val': production_budget_val,
            'marketing_budget_val': marketing_budget_val,
            'director_name': director_name,
            'production_house': production_house,
            'lead_actor': lead_actor,
            'lead_actress': lead_actress,
            'co_actors': co_actors,
            'music_director': music_director,
            'sentiment': sentiment,
            'content_themes': content_themes,
            'popularity_tags': popularity_tags
        }

        with st.spinner("Processing feature engineering & ML inference..."):
            res = predictor.predict_single(input_data)

        category = res['predicted_category']
        confidence = res['confidence']
        probs = res['probabilities']
        recs = res['recommendations']
        rep_indices = res.get('reputation_indices', {})

        st.markdown("#### Classification Output & Strategic Analytics")

        res_col1, res_col2 = st.columns([1, 1])

        with res_col1:
            card_class = "result-card-high" if category == 'High' else ("result-card-medium" if category == 'Medium' else "result-card-low")
            badge_class = "badge-high" if category == 'High' else ("badge-medium" if category == 'Medium' else "badge-low")
            fa_icon = '<i class="fa-solid fa-circle-check"></i>' if category == 'High' else ('<i class="fa-solid fa-triangle-exclamation"></i>' if category == 'Medium' else '<i class="fa-solid fa-circle-xmark"></i>')

            st.markdown(f"""
            <div class="{card_class}">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 600; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.05em;">Predicted Quality Class</span>
                    <span class="{badge_class}">{category.upper()}</span>
                </div>
                <h2 style="font-size: 2.4rem; margin: 0.6rem 0; font-weight: 700;">{fa_icon} {category} Quality</h2>
                <p style="font-size: 1rem; margin: 0;">Inference Confidence: <strong>{confidence}%</strong></p>
                <hr style="border-color: rgba(0,0,0,0.1); margin: 0.8rem 0;">
                <p style="margin: 0; font-size: 0.95rem;"><strong>Action Status:</strong> {recs['action_badge']}</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("##### Calculated Reputation Indices (CineIntelligence™ Engine)")
            if rep_indices:
                idx_col1, idx_col2 = st.columns(2)
                with idx_col1:
                    st.metric("Director Reputation Index", f"{rep_indices.get('director_index', 7.5)} / 10.0")
                    st.metric("Production Banner Index", f"{rep_indices.get('production_house_index', 7.5)} / 10.0")
                    st.metric("Music Director Index", f"{rep_indices.get('music_director_index', 7.0)} / 10.0")
                with idx_col2:
                    st.metric("Lead Actor Star Index", f"{rep_indices.get('actor_index', 7.0)} / 10.0")
                    st.metric("Lead Actress Star Index", f"{rep_indices.get('actress_index', 7.0)} / 10.0")

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("##### Class Probability Distribution")
            st.progress(probs['High'], text=f"High Rating Probability (≥ 7.5): {probs['High']*100:.1f}%")
            st.progress(probs['Medium'], text=f"Medium Rating Probability (5.5 - 7.4): {probs['Medium']*100:.1f}%")
            st.progress(probs['Low'], text=f"Low Rating Probability (< 5.5): {probs['Low']*100:.1f}%")

        with res_col2:
            st.markdown("##### Commercial Content Recommendations")
            st.info(f"**Acquisition Classification:** {recs['acquisition_tier']}")
            st.success(f"**Marketing Allocation:** {recs['marketing_strategy']}")
            st.warning(f"**Distribution Strategy:** {recs['platform_positioning']}")
            st.caption(f"**Format Classification:** {recs['short_film_note']}")

# ==========================================
# TAB 2: MODEL BENCHMARKS & METRICS
# ==========================================
with tab2:
    st.markdown("#### Machine Learning Model Evaluation Benchmarks")
    st.caption("Quantitative performance metrics evaluated on a stratified test partition.")

    eval_results = metadata.get('evaluation_results', {})

    bench_data = []
    for model_name, metrics in eval_results.items():
        bench_data.append({
            'Algorithm': model_name,
            'Accuracy': metrics['accuracy'],
            'Precision (Weighted)': metrics['precision'],
            'Recall (Weighted)': metrics['recall'],
            'F1 Score (Weighted)': metrics['f1_score'],
            'ROC-AUC Score': metrics['roc_auc']
        })

    df_bench = pd.DataFrame(bench_data)
    st.dataframe(df_bench.style.highlight_max(axis=0, color='#e0e7ff'), width="stretch")

    st.markdown("---")

    m_col1, m_col2 = st.columns(2)

    with m_col1:
        st.markdown("##### Feature Importance Drivers")
        feature_imp = metadata.get('feature_importances', {})
        if feature_imp:
            top_feats = dict(list(feature_imp.items())[:10])
            fig, ax = plt.subplots(figsize=(8, 5))
            fig.patch.set_facecolor('#ffffff')
            ax.set_facecolor('#f8fafc')
            
            y_pos = np.arange(len(top_feats))
            ax.barh(y_pos, list(top_feats.values())[::-1], color='#2563eb', edgecolor='#1d4ed8')
            ax.set_yticks(y_pos)
            ax.set_yticklabels(list(top_feats.keys())[::-1], color='#0f172a', fontsize=10)
            ax.set_xlabel("Feature Importance Score", color='#0f172a', fontweight='bold')
            ax.set_title(f"Top Predictors - {metadata['best_model_name']}", color='#0f172a', fontsize=11, fontweight='bold')
            ax.tick_params(colors='#0f172a')
            for spine in ax.spines.values():
                spine.set_color('#cbd5e1')
            st.pyplot(fig)

    with m_col2:
        st.markdown("##### Confusion Matrix")
        best_model_name = metadata.get('best_model_name', 'Gradient Boosting')
        if best_model_name in eval_results:
            cm = np.array(eval_results[best_model_name]['confusion_matrix'])
            fig, ax = plt.subplots(figsize=(6, 5))
            fig.patch.set_facecolor('#ffffff')
            ax.set_facecolor('#f8fafc')

            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
                        xticklabels=['Low', 'Medium', 'High'],
                        yticklabels=['Low', 'Medium', 'High'],
                        cbar=False)
            ax.set_xlabel("Predicted Class", color='#0f172a', fontweight='bold')
            ax.set_ylabel("Ground Truth Class", color='#0f172a', fontweight='bold')
            ax.set_title(f"Confusion Matrix ({best_model_name})", color='#0f172a', fontsize=11, fontweight='bold')
            ax.tick_params(colors='#0f172a')
            st.pyplot(fig)

# ==========================================
# TAB 3: ABOUT (CONSOLIDATED EDA & SYSTEM ARCHITECTURE)
# ==========================================
with tab3:
    st.markdown("#### About CineIntelligence™ Platform")
    st.caption("Comprehensive platform overview, Exploratory Data Analysis (EDA), and Technical Architecture.")

    about_sub1, about_sub2, about_sub3 = st.tabs([
        "Platform Overview", 
        "Dataset Explorer & EDA", 
        "System Architecture"
    ])

    with about_sub1:
        st.markdown("""
        ##### About CineIntelligence™
        **CineIntelligence™** is an enterprise AI decision-support platform engineered for film production houses, theatrical distributors, and OTT streaming platforms (*Netflix, Amazon Prime Video, Disney+ Hotstar, SonyLIV*).

        It predicts pre-release movie quality categories (`High`: $\ge 7.5$, `Medium`: $5.5 - 7.4$, `Low`: $< 5.5$) and computes real-time creative reputation metrics before principal photography or theatrical acquisition.

        ##### Core Platform Capabilities:
        - **Automated Reputation Indices (1.0 - 10.0)** for Directors, Production Houses, Actors, Actresses, & Music Composers.
        - **52+ Journal Content Themes** & Popularity Drivers.
        - **Multi-Currency & Financial Units** (`INR ₹`, `USD $`, `EUR €`, `GBP £` across `Crores`, `Lakhs`, `Millions`).
        - **Leakage-Free Machine Learning Architecture**: 80/20 Train-Test split before feature scaling and encoding.
        """)

    with about_sub2:
        st.markdown("##### Exploratory Data Analysis & Diagnostics")
        if df_data is not None:
            st.caption(f"Exploratory diagnostics across {len(df_data)} real-world movie records.")
            
            eda_col1, eda_col2 = st.columns(2)
            
            with eda_col1:
                fig, ax = plt.subplots(figsize=(7, 4.5))
                fig.patch.set_facecolor('#ffffff')
                ax.set_facecolor('#f8fafc')
                
                counts = df_data['rating_category'].value_counts()
                colors = ['#22c55e', '#f59e0b', '#ef4444']
                ax.pie(counts, labels=counts.index, autopct='%1.1f%%', colors=colors, textprops={'color': '#0f172a', 'fontsize': 10, 'weight': 'bold'})
                ax.set_title("Rating Category Distribution", color='#0f172a', fontweight='bold')
                st.pyplot(fig)

            with eda_col2:
                fig, ax = plt.subplots(figsize=(7, 4.5))
                fig.patch.set_facecolor('#ffffff')
                ax.set_facecolor('#f8fafc')
                
                sns.boxplot(data=df_data, x='rating_category', y='director_score', hue='rating_category', palette=['#ef4444', '#f59e0b', '#22c55e'], legend=False, ax=ax)
                ax.set_title("Director Reputation Score vs Rating Category", color='#0f172a', fontweight='bold')
                ax.set_xlabel("Rating Category", color='#0f172a')
                ax.set_ylabel("Director Reputation Score", color='#0f172a')
                ax.tick_params(colors='#0f172a')
                for spine in ax.spines.values():
                    spine.set_color('#cbd5e1')
                st.pyplot(fig)

            st.markdown("##### Raw Dataset Explorer")
            st.dataframe(df_data.head(20), width="stretch")
        else:
            st.warning("Dataset file missing at dataset/imdb_movies_dataset.csv.")

    with about_sub3:
        st.markdown("##### Technical System Architecture & End-to-End Flow")
        st.caption("Component interaction, data pipeline flow, and machine learning inference pipeline.")

        st.markdown("""
```mermaid
graph TD
    A[Director, Banner, Actor, Actress & Music Selectors] -->|Automated Background Reputation Engine| B[Domain Feature Engineering]
    B -->|50+ Movie Themes & Popularity Tags| C[Strict Train/Test Preprocessor]
    C -->|Scaled Feature Vector| D[ML Model Engine]
    D -->|Class Probabilities| E[Category Classifier]
    E -->|High / Medium / Low Output| F[Commercial Recommendation Matrix]
    F -->|Acquisition Tier & Marketing Strategy| G[CineIntelligence™ Dashboard]
```
        """, unsafe_allow_html=True)
