# 🩺 DiaPlate — Smart Diabetes Prediction & Culinary Recommendation System

DiaPlate adalah aplikasi web interaktif berbasis **Streamlit** dan **Machine Learning** yang dirancang untuk membantu deteksi dini risiko diabetes sekaligus memberikan rekomendasi menu kuliner sehat seimbang secara personal.

---

## 🌟 Fitur Utama
- **Smart Prediction Engine:** Memprediksi tingkat risiko diabetes (Sehat, Prediabetes, Diabetes) berbasis Machine Learning menggunakan 10 indikator utama kesehatan pasien (BRFSS).
- **Personalized Culinary Recommendation:** Menyajikan rekomendasi menu kuliner dengan penyaringan otomatis batasan kalori dan karbohidrat yang aman secara medis.
- **Dynamic Menu Selection:** Pengacakan terkontrol untuk variasi menu makanan sehat tanpa mengurangi standar nutrisi medis.
- **Modern Clean Light-Mode UI:** Tampilan antarmuka yang ramah pengguna, bersih, dan estetik dengan skema warna *Medical Blue*.

---

## 🛠️ Teknologi yang Digunakan
- **Python 3.10+**
- **Streamlit** (User Interface Framework)
- **Pandas & NumPy** (Data Processing & Manipulation)
- **Scikit-Learn & XGBoost / Random Forest** (Machine Learning Model)
- **Joblib / Pickle** (Model Serialization)

---

## 📂 Struktur File Utama
```text
diabetes-prediction/
├── app.py                           # Kode Utama Aplikasi Streamlit
├── cosine_sim_model.pkl             # Model Cosine Similarity untuk Rekomendasi
├── diabetes_prediction_model.pkl    # Model Machine Learning Prediksi Diabetes
└── foods_data.pkl                   # Reference Dataset Menu & Nutrisi Makanan
