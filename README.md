# 🌦️ UAS Prak ML – Klasifikasi Cuaca dengan CNN

## 👥 Kelompok 6
### Project UAS Praktikum Machine Learning

#### Anggota:
1. **Alvia Zuhra** (2208107010003)  
2. **Iffatun Nisa Nasrullah** (2208107010009)  
3. **Meutia Aini** (2208107010005)  
4. **Nuri Masyithah** (2208107010006)  
5. **Fazhira Risky Harmayani** (2208107010012)

---

## 📝 Deskripsi Proyek

Proyek ini merupakan implementasi klasifikasi gambar menggunakan model **Convolutional Neural Network (CNN)** untuk mengenali jenis cuaca dari gambar.

Dataset yang digunakan diambil dari Kaggle, terdiri dari gambar cuaca yang dikategorikan ke dalam **tiga kelas utama**:

- **Dew** (embun)  
- **FogSmog** (kabut atau asap)  
- **Sandstorm** (badai pasir)

Pada tahap Tugas 3, dilakukan pelatihan tiga model CNN dengan arsitektur berbeda. Hasil evaluasi menunjukkan bahwa **Model 1** memiliki performa terbaik berdasarkan **validation loss** yang paling rendah dan **validation accuracy** tertinggi. Oleh karena itu, Model 1 digunakan sebagai model utama dalam proyek ini.

Setelah model terbaik dipilih, dilakukan **deployment menggunakan Streamlit**, sehingga aplikasi dapat diakses melalui antarmuka web yang sederhana dan interaktif. Pengguna dapat mengunggah gambar dan mendapatkan prediksi jenis cuaca berdasarkan model CNN yang telah dilatih.

---

## ⚙️ Instruksi Penerapan (Deployment)

Berikut langkah-langkah untuk menjalankan aplikasi klasifikasi cuaca menggunakan **Streamlit**:

### 1. Clone repositori atau salin file proyek:
<pre> git clone https://github.com/meutiaaini/UAS.git </pre>
<pre> cd UAS </pre>

### 2. Instal semua dependensi yang dibutuhkan:
<pre> pip install -r requirements.txt </pre>

### 3. Jalankan aplikasi Streamlit:
<pre> streamlit run streamlit_app.py </pre>

💡 Fitur Aplikasi
Upload gambar cuaca melalui antarmuka web.
Aplikasi akan menampilkan:
1. Label asli dari gambar (contoh: Dew, FogSmog, atau Sandstorm)
2. Confidence score dari prediksi model (dalam persentase)


