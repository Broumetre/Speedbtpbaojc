
import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="SpeedTok Brou", page_icon="⚡", layout="wide")

st.markdown("""
<style>
.main {background-color: #000000; padding: 0px!important;}
.block-container {padding: 0px!important;}
    h1, h2, h3, p {color: white;}
.stButton>button {
        background-color: #FE2C55;
        color: white;
        border-radius: 8px;
        border: none;
        height: 45px;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return YOLO('yolov8n.pt')

model = load_model()

if 'video_index' not in st.session_state:
    st.session_state.video_index = 0

videos_ick = [
    {"auteur": "@Brou_ICK", "desc": "Coulage poteaux R+1 #BTS2026", "likes": 247, "image": "https://i.imgur.com/8tK1Z9G.jpg"},
    {"auteur": "@Kouame_GC", "desc": "Ferraillage poutre 20x40 #SpeedMetre", "likes": 189, "image": "https://i.imgur.com/5X6wQyL.jpg"},
    {"auteur": "@Prof_Coulibaly", "desc": "Correction métré TD3 #ICK", "likes": 512, "image": "https://i.imgur.com/3Z9n9xP.jpg"},
]

current_video = videos_ick[st.session_state.video_index % len(videos_ick)]

col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.markdown("<h1 style='text-align: center;'>⚡ SpeedTok</h1>", unsafe_allow_html=True)

st.image(current_video["image"], use_column_width=True)

st.markdown(f"""
<div style='position: relative; top: -150px; padding: 20px;'>
    <h3 style='margin: 0px;'>{current_video["auteur"]}</h3>
    <p style='margin: 0px;'>{current_video["desc"]}</p>
    <p style='margin: 0px;'>🎵 Son original - Bruit de bétonnière</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([6,1])
with col2:
    st.markdown("<div style='position: relative; top: -400px;'>", unsafe_allow_html=True)
    if st.button("❤️", key="like"):
        current_video["likes"] += 1
    st.markdown(f"<p style='text-align: center;'>{current_video['likes']}</p>", unsafe_allow_html=True)
    st.button("💬", key="com")
    st.markdown("<p style='text-align: center;'>12</p>", unsafe_allow_html=True)
    st.button("📤", key="share")
    st.markdown("<p style='text-align: center;'>Partager</p>", unsafe_allow_html=True)
    if st.button("⚡", key="scan"):
        with st.spinner('SpeedMetre by Brou scanne...'):
            results = model(current_video["image"])
            nb = len(results[0].boxes)
            st.toast(f"SpeedTok: {nb} éléments détectés! Béton ≈ {nb*0.12:.1f}m³", icon="⚡")
    st.markdown("</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("👆 SWIPE UP - Chantier suivant", use_container_width=True):
        st.session_state.video_index += 1
        st.rerun()

st.caption("SpeedTok © 2026 - Créé par Brou - BTS 1 Génie Civil ICK Bouaké 🇨🇮")
