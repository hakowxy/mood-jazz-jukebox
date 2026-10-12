import random

import streamlit as st

from jukebox import LOCATIONS, MUSIC_DATA, recommend_music, vibe_label

st.set_page_config(page_title="mood jukebox", layout="wide")

# --- kawaii minimal styling ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Indie+Flower&family=Gochi+Hand&display=swap');

    .stApp {
        background-color: #284d3c;
        color: #FFFFFF;
        font-family: 'Indie Flower', 'Gochi Hand', cursive;
        font-size: 1.4em;
        text-transform: lowercase;
    }
    h1, h2, h3 {
        color: #FF69B4 !important;
        font-family: 'Indie Flower', 'Gochi Hand', cursive;
        font-weight: 900;
        text-shadow: 2px 2px 3px rgba(0, 0, 0, 0.6);
        text-transform: lowercase;
    }

    /* keep every label and option readable on the dark green background */
    [data-testid="stForm"] label, [data-testid="stRadio"] label, .stSlider > label {
        color: #FFFFFF !important;
        text-transform: lowercase;
        font-family: 'Indie Flower', 'Gochi Hand', cursive;
    }

    /* square, pink-and-white radio buttons */
    [data-testid="stRadio"] input[type="radio"] + div::before {
        border-radius: 0% !important;
        width: 18px;
        height: 18px;
        background-color: #FFFFFF !important;
        border: 2px solid #FF69B4 !important;
    }
    [data-testid="stRadio"] input[type="radio"]:checked + div::before {
        background-color: #FF69B4 !important;
        border: 4px solid #FFFFFF !important;
    }

    /* cream button */
    .stButton>button {
        background-color: #F5F5DC;
        color: #FF69B4;
        border: 3px solid #FF69B4;
        font-weight: 700;
        border-radius: 12px;
        font-family: 'Indie Flower', 'Gochi Hand', cursive;
        font-size: 1.4em;
        text-transform: lowercase;
    }
    .stButton>button:hover { background-color: #f0f0c9; }

    /* slider knob */
    .stSlider [data-testid="stTickBar"] div { color: #FFFFFF !important; }
    .stSlider [data-testid="stThumbValue"] {
        background-color: #FF69B4;
        border: 2px solid #FFFFFF;
        color: #FFFFFF !important;
    }
    .stSlider [data-testid="stTrack"] { background: linear-gradient(to right, #F5F5DC, #FF69B4); }

    /* falling decorations */
    @keyframes snowfall { 0% {top: -10%;} 100% {top: 100%;} }
    .snowflake {
        color: #FFFFFF;
        position: fixed;
        z-index: 9999;
        user-select: none;
        pointer-events: none;
        animation: snowfall linear infinite;
    }
    .snowflake:nth-child(1) { left: 5%;  font-size: 1.5em; animation-duration: 10s; animation-delay: 0s; }
    .snowflake:nth-child(2) { left: 15%; font-size: 1.0em; animation-duration: 15s; animation-delay: 2s; }
    .snowflake:nth-child(3) { left: 25%; font-size: 1.8em; animation-duration: 12s; animation-delay: 4s; }
    .snowflake:nth-child(4) { left: 40%; font-size: 1.3em; animation-duration: 18s; animation-delay: 6s; }
    .snowflake:nth-child(5) { left: 60%; font-size: 1.6em; animation-duration: 11s; animation-delay: 8s; }
    .snowflake:nth-child(6) { left: 80%; font-size: 1.1em; animation-duration: 16s; animation-delay: 10s; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="snowflake">💖</div>
    <div class="snowflake">⭐</div>
    <div class="snowflake">🎄</div>
    <div class="snowflake">🎀</div>
    <div class="snowflake">❄️</div>
    <div class="snowflake">⭐</div>
""", unsafe_allow_html=True)

st.title("mood jukebox")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### set your mood dial")
    mood_score = st.slider("turn the knob: 1 (cozy) to 10 (sparkly)", min_value=1, max_value=10, value=6)
    st.markdown(f"**current vibe:** {vibe_label(mood_score)}")

with col2:
    st.markdown("### scene location")
    location = st.radio("where are you listening?", options=LOCATIONS, index=0)
    st.markdown(f"**scene selected:** {location}")

st.markdown("---")

if st.button("get vibe"):
    genre = recommend_music(mood_score, location)
    track_url = random.choice(MUSIC_DATA[genre])
    st.subheader(f"recommended: {genre} 🎶")
    st.markdown(f"""
        <iframe src="{track_url}" width="100%" height="350" frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen></iframe>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("from xinyangma18")
