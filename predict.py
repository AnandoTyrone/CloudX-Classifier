import numpy as np
import os 
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# 1. SET LOKASI PATH ABSOLUT MODEL SECARA AMAN
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model_klasifikasi_awan.h5')

print("🔄 Sedang memuat model AI ke memori lokal...")

# 2. MUAT MODEL TENSORFLOW (CUKUP 1 KALI SAJA)
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("✅ Model klasifikasi awan berhasil dimuat dengan sempurna!")
except Exception as e:
    print(f"❌ GAGAL MEMUAT MODEL! Eror asli dari TensorFlow: {e}")
    print("Pastikan file 'model_klasifikasi_awan.keras' berada di folder yang sama dengan script ini.")
    exit()

# 3. DAFTAR 10 KELAS AWAN (URUTAN WAJIB SAMA DENGAN DATASET)
class_names = [
    'Altocumulus', 'Altostratus', 'Cirrocumulus', 'Cirrostratus', 'Cirrus',
    'Cumulonimbus', 'Cumulus', 'Nimbostratus', 'Stratocumulus', 'Stratus'
]

def prediksi_jenis_awan(image_path):
    # Validasi keselamatan: Cek apakah file gambar target memang ada
    if not os.path.exists(image_path):
        print(f"⚠️ Eror: File gambar '{image_path}' tidak ditemukan! Silakan periksa kembali path fotonya.")
        return

    # Prapemrosesan Gambar Target (Dimensi 224x224)
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) # Ubah ke bentuk batch (1, 224, 224, 3)
    img_array = img_array.astype(np.float32)

    # PERBAIKAN UTAMA: Menggunakan fungsi normalisasi bawaan MobileNetV2 (-1 s.d +1)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)

    # Eksekusi Prediksi AI 
    predictions = model.predict(img_array)
    
    # Mengambil indeks dengan nilai probabilitas tertinggi
    highest_prob_index = np.argmax(predictions[0])
    
    # Mendapatkan nama label awan dan skor kepercayaannya 
    label_awan = class_names[highest_prob_index]
    confidence_score = predictions[0][highest_prob_index] * 100

    # Tampilan Output Akhir di Terminal (Sesuai Standar Proposal Proyek)
    print("\n" + "="*45)
    print("      HASIL DETEKSI AI VISI KOMPUTER")
    print("="*45)
    print(f" Jenis Awan       : {label_awan}")
    print(f" Confidence Score : {confidence_score:.2f}%")
    print("="*45)

# --- CARA TESTING DI LAPTOP / VS CODE ---
# Ganti nama file di bawah ini dengan foto awan asli yang ingin kamu tes di folder proyekmu
test_image_path = "awan_cumulonimbus_test.jpg" 
prediksi_jenis_awan(test_image_path)