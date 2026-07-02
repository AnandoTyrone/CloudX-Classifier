import streamlit as st
import os 
import numpy as np
from PIL import Image

# 1. GUNAKAN KERAS MURNI UNTUK PEMUATAN MODEL (Bypass Bug tf.keras)
try:
    import keras
    from keras.applications.mobilenet_v2 import preprocess_input
except ImportError:
    import tensorflow as tf
    from tensorflow import keras
    from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# DEFINISIKAN PATH ABSOLUT GLOBAL
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model_klasifikasi_awan.keras')

@st.cache_resource
def load_my_model(path):
    # Menggunakan keras murni untuk menghindari error deserialisasi Keras 3
    return keras.models.load_model(path)

def show_klasifikasi():
    # HEADER KLASIFIKASI SIMETRIS
    st.markdown("<h1 style='text-align: center; color: #0369a1; font-family: sans-serif; font-weight: 800; font-size: 2.5rem; margin-bottom: 0px;'>☁️ CloudX Intelligent Classifier</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #475569; font-size: 1.15rem; margin-top: 5px; margin-bottom: 0px;'>Unggah foto atmosfer Anda untuk mengidentifikasi jenis awan secara otomatis.</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='premium-bar'></div>", unsafe_allow_html=True)

    # MUAT MODEL CACHED SECARA AMAN
    try:
        model = load_my_model(MODEL_PATH)
    except Exception as e:
        st.error(f"Gagal memuat model. Eror asli dari Keras/TensorFlow: {e}")
        st.warning("Pastikan file 'model_klasifikasi_awan.keras' sudah sukses terunggah di repositori GitHub Anda.")
        return
    
    class_names = [
        'Altocumulus', 'Altostratus', 'Cirrocumulus', 'Cirrostratus', 'Cirrus',
        'Cumulonimbus', 'Cumulus', 'Nimbostratus', 'Stratocumulus', 'Stratus'
    ]

    st.markdown("<h4 style='text-align: center; color: #334155; font-weight: 600;'>📸 Unggah Citra Awan</h4>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Pilih file foto atmosfer atau seret gambar ke sini...", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

    if uploaded_file is not None:
        st.markdown("<div class='premium-bar' style='height: 1px; opacity: 0.2;'></div>", unsafe_allow_html=True)
        
        # Grid Layout Seimbang Kiri & Kanan
        col_img, col_res = st.columns([1, 1], gap="large")
        
        with col_img:
            image = Image.open(uploaded_file)
            st.markdown("<div style='text-align: center; font-weight: bold; color: #475569; margin-bottom: 5px;'>Gambar Input</div>", unsafe_allow_html=True)
            st.image(image, use_container_width=True)
        
        with col_res:
            with st.spinner("🔄 Mengekstraksi fitur visual citra awan..."):
                img_resized = image.resize((224, 224))
                img_array = np.array(img_resized)
                if img_array.shape[-1] == 4:  
                    img_array = img_array[:, :, :3]
                
                img_array = np.expand_dims(img_array, axis=0)
                img_array = img_array.astype(np.float32)
                
                # Memproses gambar sesuai arsitektur MobileNetV2
                img_array = preprocess_input(img_array)
                
                predictions = model.predict(img_array)
                highest_prob_index = np.argmax(predictions[0])
                
                label_awan = class_names[highest_prob_index]
                confidence_score = predictions[0][highest_prob_index] * 100
            
            st.markdown(f"""
                <div style='background-color: #ffffff; padding: 22px; border-radius: 16px; border-left: 6px solid #0284c7; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05); margin-bottom: 15px;'>
                    <p style='margin:0; font-size:0.85rem; color:#64748b; font-weight:bold; text-transform:uppercase; tracking-spacing: 1px;'>Hasil Analisis AI</p>
                    <h2 style='margin:5px 0; color:#0369a1; font-size:2.2rem; font-weight:800;'>{label_awan}</h2>
                    <p style='margin:0; font-size:1.05rem; color:#0f172a;'>Confidence Percentage: <b>{confidence_score:.2f}%</b></p>
                </div>
            """, unsafe_allow_html=True)
            
            st.progress(int(confidence_score))
            
            # Dampak Sektor Navigasi Udara
            st.markdown("<p style='font-weight: 700; color: #1e293b; margin-top: 15px; margin-bottom: 5px;'>✈️ Dampak Navigasi Udara:</p>", unsafe_allow_html=True)
            if label_awan == "Cumulonimbus":
                st.error("⚠️ **BAHAYA EKSTREM!** Terdeteksi struktur awan Cumulonimbus. Risiko badai petir, turbulensi parah, dan icing pesawat. Jalur penerbangan wajib dialihkan demi keselamatan.")
            elif label_awan in ["Nimbostratus", "Stratus"]:
                st.warning("🌧️ **PERINGATAN CUACA:** Terdeteksi awan pembawa hujan/presipitasi rendah. Jarak pandang (visibility) berkurang, disarankan pilot meningkatkan kewaspadaan instrumen.")
            else:
                st.success("☀️ **KONDISI AMAN:** Jenis awan ini berada di tingkat yang stabil dan aman, tidak membawa potensi cuaca ekstrem yang mengganggu keselamatan navigasi penerbangan.")

    st.markdown("<br><br><div class='premium-bar' style='height: 2px; opacity:0.3;'></div>", unsafe_allow_html=True)
    st.caption("<p style='text-align: center; color: #94a3b8;'>Proyek Individu Computer Vision • Pengembangan Sistem Klasifikasi Awan Otomatis</p>", unsafe_allow_html=True)