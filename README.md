🛡️ Spam Detector
Proyek ini adalah implementasi sederhana Spam Detector menggunakan Python dan algoritma Naive Bayes. Sistem ini mengklasifikasikan pesan teks apakah termasuk spam atau bukan spam (ham) menggunakan pendekatan machine learning klasik berbasis probabilitas.

Cocok untuk pembelajaran dasar tentang:

Preprocessing teks

Ekstraksi fitur (Bag of Words)

Klasifikasi Naive Bayes

Evaluasi model machine learning

✨ Fitur
✅ Menggunakan algoritma Multinomial Naive Bayes

✅ Dataset dapat dimodifikasi sendiri

✅ Tidak butuh koneksi internet atau API Key

✅ Ringan dan cepat dijalankan di laptop biasa

🛠️ Prasyarat
Python 3.x

Pustaka:

scikit-learn

pandas

nltk (untuk preprocessing teks)

Instalasi:

bash
Salin
Edit
pip install scikit-learn pandas nltk
📁 Struktur Proyek
bash
Salin
Edit
├── spam_detector.py        # Script utama untuk training dan prediksi
├── spam_dataset.csv        # Dataset spam/ham (SMS atau email)
├── README.md               # Dokumentasi proyek
🚀 Contoh Penggunaan
bash
Salin
Edit
$ python spam_detector.py
Masukkan pesan: kamu menang undian hadiah 1 miliar
Hasil: SPAM

Masukkan pesan: saya akan datang ke kantor besok
Hasil: HAM (bukan spam)
