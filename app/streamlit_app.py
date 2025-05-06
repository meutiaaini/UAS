import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Load model
model = load_model('D:\\Coeleyah sem 6\\ML\\LAB\\UAS\\Model\\model1.h5')  # Sesuaikan path

# Label dictionary
label_dict = {0: 'dew', 1: 'fogsmog', 2: 'sandstorm'}
threshold = 0.6 # Jika confidence < 0.7, dianggap bukan dari 3 label

# Preprocessing function
def preprocess_image(image):
    image = image.convert("RGB")  # Pastikan format RGB
    image = image.resize((224, 224))  # Ukuran sesuai input model
    image = img_to_array(image) / 255.0  # Normalisasi
    image = np.expand_dims(image, axis=0)  # Tambah dimensi batch
    return image

# Streamlit UI
st.title("Weather Classifier (dew, fogsmog, sandstorm)")

uploaded_file = st.file_uploader("Upload gambar hewan", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar yang diupload", use_column_width=True)

    # Preprocess & Predict
    processed = preprocess_image(image)
    # Setelah mendapatkan prediksi dari model
    predictions = model.predict(processed)[0]
    predicted_idx = np.argmax(predictions)
    confidence = float(np.max(predictions))
    predicted_label = label_dict[predicted_idx]

    if confidence >= threshold:
        st.markdown(f"### Prediksi: **{predicted_label.upper()}**")
        st.markdown(f"### Confidence Score: **{confidence:.2f}**")
    else:
        st.warning("Gambar tidak dikenali sebagai dew, fogsmog, dan sandstorm.")
        st.markdown(f"### Confidence tertinggi hanya: **{confidence:.2f}**")
