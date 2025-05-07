# UAS Prak ML

# Kelompok : 6
# Project UAS Praktikum Machine Learning
### Anggota
1. Alvia Zuhra (2208107010003)
2. Iffatun Nisa Nasrullah (2208107010009)
3. Meutia Aini (2208107010005)
4. Nuri Masyithah (2208107010006)
5. Fazhira Risky Harmayani (2208107010012)

📝 Deskripsi Proyek
Proyek ini merupakan implementasi klasifikasi gambar menggunakan model Convolutional Neural Network (CNN) untuk mengenali jenis cuaca dari gambar. Dataset diambil dari Kaggle, yang terdiri dari gambar cuaca yang dikategorikan ke dalam tiga kelas utama:
1. Dew (embun)
2. FogSmog (kabut atau asap)
3. Sandstorm (badai pasir)
Pada tahap Tugas 3, dilakukan pelatihan tiga model CNN dengan arsitektur berbeda. Hasil evaluasi menunjukkan bahwa Model 1 memiliki performa terbaik dengan validation loss paling rendah dan validation accuracy tertinggi, sehingga model ini dipilih sebagai model utama.
Setelah model terbaik dipilih, dilakukan deployment menggunakan Streamlit agar dapat diakses melalui antarmuka web yang sederhana dan interaktif. Aplikasi ini memungkinkan pengguna mengunggah gambar dan mendapatkan prediksi jenis cuaca berdasarkan model CNN yang telah dilatih.

⚙️ Instruksi Penerapan (Deployment)
Berikut langkah-langkah untuk menjalankan aplikasi klasifikasi cuaca menggunakan Streamlit:
1. Clone repositori atau salin file proyek.
   pip install -r requirements.txt
2. Pastikan sudah menginstal semua dependensi yang dibutuhkan:
   streamlit run app.py
3. Pada halaman web, pengguna dapat mengunggah gambar cuaca. Aplikasi akan menampilkan:
   Label asli (misalnya: Dew, FogSmog, atau Sandstorm)
   Confidence score untuk prediksi tersebut (dalam persentase)
