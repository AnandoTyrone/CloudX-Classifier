import streamlit as st

# 1. KONFIGURASI HALAMAN UTAMA
st.set_page_config(
    page_title="CloudX - Sistem Analisis Awan",
    page_icon="☁️",
    layout="centered"
)

# 2. SELERASI DESAIN GLOBAL & ANIMASI BACKGROUND GAMBAR AWAN BERGANTI OTOMATIS
st.markdown("""
    <style>
    /* Animasi Perubahan Gambar Latar Belakang Awan Realistis */
    @keyframes cloudCycler {
        0% { background-image: url('https://images.unsplash.com/photo-1534088568595-a066f410bcda?q=80&w=1600'); } /* Cirrus */
        30% { background-image: url('https://images.unsplash.com/photo-1504608524841-42fe6f032b4b?q=80&w=1600'); } /* Cumulus */
        65% { background-image: url('https://images.unsplash.com/photo-1513002749550-c59d786b8e6c?q=80&w=1600'); } /* Altocumulus */
        100% { background-image: url('https://images.unsplash.com/photo-1432057322224-8916b9ed202a?q=80&w=1600'); } /* Cumulonimbus */
    }
    
    .stApp {
        animation: cloudCycler 30s infinite alternate ease-in-out;
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Lapisan Efek Kaca Transparan (Glassmorphism) Utama agar Teks Sangat Jelas Dibaca */
    .stMainBlockContainer {
        background-color: rgba(255, 255, 255, 0.92) !important;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        padding: 3rem !important;
        border-radius: 24px !important;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.12) !important;
        border: 1px solid rgba(255, 255, 255, 0.5);
        margin-top: 2rem;
        margin-bottom: 2rem;
    }
    
    /* Dekorasi Garis Pembatas (Aksen Bar) Premium */
    .premium-bar {
        height: 5px;
        background: linear-gradient(90deg, #38bdf8 0%, #0284c7 50%, #0369a1 100%);
        border-radius: 10px;
        margin: 1.5rem auto;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# 3. IMPORT HALAMAN
from home import show_home
from klasifikasi import show_klasifikasi

# 4. SISTEM NAVIGASI MULTI-HALAMAN
page_home = st.Page(show_home, title="Home", icon="🏠")
page_klasifikasi = st.Page(show_klasifikasi, title="Klasifikasi", icon="📊")

pg = st.navigation([page_home, page_klasifikasi])
pg.run()