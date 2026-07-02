import numpy as np
import os 
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# 1. Load Model yang Sudah Dilatih 
model = tf.keras.models.load_model("model_klasifikasi_awan.keras")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model_klasifikasi_awan.keras')

# 2. Muat model dan pancing eror aslinya jika gagal
try:
    # Menggunakan MODEL_PATH absolut agar server tidak tersesat mencari file
    model = tf.keras.models.load_model(MODEL_PATH)
except Exception as e:
    # Kode ini akan menampilkan biang kerok eror yang sesungguhnya di layar web
    st.error(f"Gagal memuat model. Eror asli dari TensorFlow: {e}")
# Contoh penulisan di dalam fungsi klasifikasi Anda:
try:
    model = tf.keras.models.load_model(MODEL_PATH)
except Exception as e:
    st.error(f"Gagal memuat model. Eror asli dari TensorFlow: {e}")
    
# 2. Daftar 10 Kelas Awan (Pastikan urutannya sama persis dengan folder dataset) [cite: 20]
class_names = [
    'Altocumulus', 'Altostratus', 'Cirrocumulus', 'Cirrostratus', 'Cirrus',
    'Cumulonimbus', 'Cumulus', 'Nimbostratus', 'Stratocumulus', 'Stratus'
] # Total 10 Jenis Awan [cite: 20, 25, 27, 29]

def prediksi_jenis_awan(image_path):
    # Preprocessing gambar input agar sesuai format training (224x224) 
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) # Mengubah ke bentuk batch (1, 224, 224, 3)
    img_array = img_array / 255.0                 # Normalisasi nilai piksel 

    # Melakukan prediksi 
    predictions = model.predict(img_array)
    
    # Mengambil indeks dengan nilai probabilitas tertinggi
    highest_prob_index = np.argmax(predictions[0])
    
    # Mendapatkan nama label awan dan skor kepercayaannya 
    label_awan = class_names[highest_prob_index]
    confidence_score = predictions[0][highest_prob_index] * 100

    # Output Jawaban Akhir (Sesuai Target Output Proposal Anda) 
    print("\n" + "="*40)
    print("      HASIL DETEKSI VISI KOMPUTER")
    print("="*40)
    print(f"Jenis Awan       : {label_awan}")
    print(f"Confidence Score : {confidence_score:.2f}%") # Contoh output: 'Cumulonimbus - 95%' 
    print("="*40)

# --- CARA MENGGUNAKAN ---
# Ganti dengan path foto awan yang ingin Anda tes di laptop/VS Code Anda
test_image_path = "awan_cumulonimbus_test.jpg" 
prediksi_jenis_awan(test_image_path)