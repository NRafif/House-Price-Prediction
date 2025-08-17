# 🏠 Prediksi Harga Rumah  

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)  
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikit-learn)  
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)  
![License](https://img.shields.io/badge/License-MIT-lightgrey)  

Proyek ini merupakan implementasi **Machine Learning** untuk memprediksi harga rumah berdasarkan berbagai fitur seperti luas bangunan, jumlah kamar, lokasi, dan karakteristik lainnya.  

## 📌 Tujuan
- Melakukan eksplorasi data (EDA) untuk memahami pola dan distribusi fitur.  
- Membangun pipeline preprocessing (handling missing values, encoding kategorikal, scaling numerik).  
- Membangun dan membandingkan performa beberapa model regresi.  
- Mengevaluasi hasil prediksi menggunakan metrik regresi.  

## 📂 Struktur Proyek
├── data/
│ ├── housing_train.csv # Dataset utama
│ └── housing_test.csv # Dataset uji
├── HousePricing.ipynb # Notebook utama
└── README.md # Dokumentasi proyek


## 🔧 Tools & Library
- Python 3.x  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- (Opsional) XGBoost / LightGBM  

## 🔍 Alur Pengerjaan
1. **Import library & load data**  
2. **EDA & visualisasi**  
   - Distribusi harga rumah  
   - Korelasi antar fitur  
   - Deteksi outlier  
3. **Data preprocessing**  
   - Menangani missing values  
   - Encoding fitur kategorikal  
   - Scaling fitur numerik  
4. **Modeling**  
   - Regresi Linear  
   - Decision Tree / Random Forest  
   - XGBoost (opsional)  
5. **Evaluasi**  
   - Metrik: MAE, RMSE, R²  
   - Visualisasi prediksi vs aktual  

## 📊 Hasil
- Model terbaik: **(isi sesuai hasilmu, misalnya Random Forest Regressor)**  
- Nilai evaluasi: **(contoh: RMSE = 23.5, R² = 0.87)**  
- Fitur paling berpengaruh: **(isi hasil feature importance)**  

## 🚀 Pengembangan Selanjutnya
- Menambahkan **feature engineering** (misalnya interaksi antar variabel).  
- Hyperparameter tuning lebih mendalam.  
- Deployment model sebagai aplikasi web dengan **Streamlit** atau **Flask**.  

---
