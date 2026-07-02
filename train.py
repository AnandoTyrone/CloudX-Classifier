import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# 1. PREPROCESSING & RE-SCALE STANDAR MOBILENETV2
IMAGE_SIZE = (224, 224) 
BATCH_SIZE = 32

# PERBAIKAN PATH: Folder harus diarahkan langsung ke 'train' dan 'test'
TRAIN_DIR = "dataset/Howard-Cloud-X/train" 
TEST_DIR = "dataset/Howard-Cloud-X/test"

# MENGGUNAKAN PREPROCESS_INPUT BAWAAN MOBILENETV2 (Skala -1 s.d +1)
train_datagen = ImageDataGenerator(
    preprocessing_function=tf.keras.applications.mobilenet_v2.preprocess_input,
    rotation_range=30,         
    width_shift_range=0.2,
    height_shift_range=0.2,
    zoom_range=0.2,           
    horizontal_flip=True,
    fill_mode='nearest'        
)

val_datagen = ImageDataGenerator(
    preprocessing_function=tf.keras.applications.mobilenet_v2.preprocess_input
)

train_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='sparse',     
)

val_generator = val_datagen.flow_from_directory(
    TEST_DIR,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='sparse',     
)

class_names = list(train_generator.class_indices.keys())
print("Daftar 10 Kelas Awan :", class_names)

# 2. MODEL DEVELOPMENT (MobileNetV2)
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)

# --- TAHAP 1: FEATURE EXTRACTION (5 EPOCH) ---
base_model.trainable = False 

# PERBAIKAN STRUKTUR ATAS: Lapisan Jauh Lebih Padat (512 -> 128) & Kebal Overfitting
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.BatchNormalization(),
    
    # Lapisan Dense Pertama untuk Ekstraksi Fitur Tekstur Berat
    layers.Dense(512, activation='relu'),
    layers.BatchNormalization(),
    layers.Dropout(0.5),
    
    # Lapisan Dense Kedua untuk Menyaring Fitur Spesifik 10 Kelas Awan
    layers.Dense(128, activation='relu'),
    layers.BatchNormalization(),
    layers.Dropout(0.3),
    
    layers.Dense(10, activation='softmax') 
])

# Learning rate 0.0005 ideal untuk pemanasan arsitektur baru yang lebih dalam
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0005), 
    loss='sparse_categorical_crossentropy', 
    metrics=['accuracy']
)

print("\n=======================================================")
print(" Memulai Training Tahap 1: Pemanasan Lapisan Atas (5 Epoch)")
print("=======================================================")
model.fit(train_generator, validation_data=val_generator, epochs=5)


# --- TAHAP 2: FINE-TUNING UTUH (50 EPOCH) ---
print("\n=======================================================")
print(" Memulai Training Tahap 2: Fine-Tuning MobileNetV2 (50 Epoch)")
print("=======================================================")

base_model.trainable = True
# Membuka 50 layer teratas agar model sensitif terhadap serat tipis awan tinggi
for layer in base_model.layers[:-50]: 
    layer.trainable = False

# PERBAIKAN OPTIMIZER: Menggunakan SGD Momentum untuk Menembus Stagnasi Val_Loss
model.compile(
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.0001, momentum=0.9), 
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Mengatur ketahanan EarlyStopping menjadi 10 epoch agar lebih sabar berkembang
early_stop = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',     
    patience=10,               
    restore_best_weights=True 
)

history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=50,             
    callbacks=[early_stop]   
)

# 4. SAVE MODEL TERBAIK
# Simpan model ke format legacy .h5 yang sangat stabil di semua versi server Linux
model.save("model_klasifikasi_awan.h5")
print("✅ Model sukses disimpan dalam format HDF5 (.h5)!")
print(train_generator.class_indices)
print("\n🎉 Model cerdas yang sesungguhnya berhasil disimpan!")