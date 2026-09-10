import joblib
import numpy as np
import pandas as pd
import pickle
import streamlit as st

# ---------------------------------------------------------
# 1. Konfigurasi Halaman & Memuat Model
# ---------------------------------------------------------
st.set_page_config(
    page_title="DiaPlate — Smart Diabetes & Nutrition System",
    page_icon="🩺",
    layout="wide",
)

# 🎨 Custom CSS Overrides (Paksa Mode Terang & Putih Bersih)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Hilangkan Header Default Streamlit */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
    }

    /* Background Utama Light Blue */
    .stApp {
        background: linear-gradient(180deg, #e0f2fe 0%, #f0f9ff 40%, #ffffff 100%) !important;
        color: #0f172a !important;
    }

    /* Hero Header Clean Modern */
    .hero-container {
        background: linear-gradient(135deg, #2563eb 0%, #0284c7 100%);
        padding: 2.5rem 2rem;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 25px -5px rgba(2, 132, 199, 0.25);
        margin-bottom: 2rem;
    }

    .hero-title {
        font-size: 2.8rem !important;
        font-weight: 800 !important;
        color: #ffffff !important;
        letter-spacing: -0.5px;
        margin-bottom: 0.25rem !important;
    }

    .hero-subtitle {
        font-size: 1.05rem;
        color: #e0f2fe;
        font-weight: 500;
    }

    .section-header {
        color: #0369a1;
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 1.25rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* Label Input */
    .stApp label p, label {
        color: #1e293b !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
    }

    /* PAKSA TEXT BOX / SELECT BOX / NUMBER INPUT BERWARNA PUTIH */
    div[data-baseweb="select"] > div, 
    div[data-baseweb="input"] > div,
    div[data-baseweb="input"] input,
    div[data-testid="stNumberInput"] input,
    .stSelectbox div[role="combobox"],
    div[role="option"] {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border-radius: 10px !important;
    }

    /* Border Input */
    div[data-baseweb="select"] > div, 
    div[data-baseweb="input"] > div {
        border: 1.5px solid #cbd5e1 !important;
        background-color: #ffffff !important;
    }

    div[data-baseweb="select"] > div:hover, 
    div[data-baseweb="input"] > div:hover {
        border-color: #0284c7 !important;
    }

    /* Tombol Plus Minus pada Number Input */
    div[data-testid="stNumberInput"] button {
        background-color: #f1f5f9 !important;
        color: #1e293b !important;
        border: none !important;
    }

    div[data-testid="stNumberInput"] button:hover {
        background-color: #e2e8f0 !important;
        color: #0284c7 !important;
    }

    /* Custom Clean Blue Button */
    .stButton > button {
        background-color: #0284c7 !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        border: none !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        padding: 0.85rem 2rem !important;
        width: 100%;
        box-shadow: 0 4px 12px rgba(2, 132, 199, 0.2) !important;
        transition: all 0.2s ease-in-out !important;
    }

    .stButton > button:hover {
        background-color: #0369a1 !important;
        box-shadow: 0 6px 16px rgba(2, 132, 199, 0.3) !important;
    }

    /* PAKSA TABEL MENJADI TERANG & ELEGAN */
    .table-container {
        background-color: #ffffff;
        border-radius: 16px;
        padding: 1rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        border: 1px solid #e2e8f0;
    }

    table.custom-table {
        width: 100%;
        border-collapse: collapse;
        background-color: #ffffff !important;
        color: #0f172a !important;
    }

    table.custom-table th {
        background-color: #f0f9ff !important;
        color: #0369a1 !important;
        text-align: left;
        padding: 14px 16px;
        font-weight: 700;
        font-size: 0.9rem;
        border-bottom: 2px solid #bae6fd;
    }

    table.custom-table td {
        padding: 12px 16px;
        border-bottom: 1px solid #f1f5f9;
        color: #334155 !important;
        font-size: 0.9rem;
        background-color: #ffffff !important;
    }

    table.custom-table tr:hover td {
        background-color: #f8fafc !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# 2. Pemuatan Assets
# ---------------------------------------------------------
@st.cache_resource
def load_assets():
    try:
        with open("diabetes_prediction_model.pkl", "rb") as f:
            diabetes_model = pickle.load(f)
    except Exception:
        diabetes_model = joblib.load("diabetes_prediction_model.pkl")

    try:
        foods_data = joblib.load("foods_data.pkl")
    except Exception as e:
        raise Exception(f"File 'foods_data.pkl' bermasalah/rusak! Detail: {e}")

    return diabetes_model, foods_data


try:
    diabetes_model, foods_data = load_assets()
    foods_df = (
        pd.DataFrame(foods_data)
        if not isinstance(foods_data, pd.DataFrame)
        else foods_data
    )
except Exception as e:
    st.error(f"❌ Error Pemuatan File: {e}")
    st.stop()

# ---------------------------------------------------------
# 3. Hero Header
# ---------------------------------------------------------
st.markdown(
    """
    <div class="hero-container">
        <div class="hero-title">DiaPlate</div>
        <div class="hero-subtitle">Smart Diabetes Prediction & Personal Nutrition Intelligence</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 4. Form Input Data Pasien
# ---------------------------------------------------------
st.markdown('<div class="section-header">📋 Input Indikator Kesehatan Utama Pasien</div>', unsafe_allow_html=True)

age_options = {
    "18 - 24 tahun": 1.0,
    "25 - 29 tahun": 2.0,
    "30 - 34 tahun": 3.0,
    "35 - 39 tahun": 4.0,
    "40 - 44 tahun": 5.0,
    "45 - 49 tahun": 6.0,
    "50 - 54 tahun": 7.0,
    "55 - 59 tahun": 8.0,
    "60 - 64 tahun": 9.0,
    "65 - 69 tahun": 10.0,
    "70 - 74 tahun": 11.0,
    "75 - 79 tahun": 12.0,
    "80+ tahun": 13.0,
}

col1, col2 = st.columns(2, gap="large")

with col1:
    highbp_opt = st.selectbox("Tekanan Darah Tinggi (Hipertensi)", ["Tidak", "Ya"])
    highchol_opt = st.selectbox("Kolesterol Tinggi", ["Tidak", "Ya"])
    bmi = st.number_input(
        "Indeks Massa Tubuh (BMI)",
        min_value=10.0,
        max_value=98.0,
        value=24.5,
        step=0.1,
    )
    genhlth = st.slider(
        "Kondisi Kesehatan Umum (1: Sangat Baik — 5: Buruk)", 1, 5, 2
    )
    physhlth = st.slider(
        "Jumlah Hari Sakit Fisik (dalam 30 Hari Terakhir)", 0, 30, 0
    )

with col2:
    selected_age_label = st.selectbox(
        "Kelompok Usia",
        list(age_options.keys()),
        index=6,
    )
    age_val = age_options[selected_age_label]
    heartdisease_opt = st.selectbox(
        "Riwayat Penyakit / Serangan Jantung", ["Tidak", "Ya"]
    )
    cholcheck_opt = st.selectbox("Rutin Cek Kolesterol (5 Tahun Terakhir)", ["Ya", "Tidak"])
    smoker_opt = st.selectbox("Perokok (Minimal 100 Batang Seumur Hidup)", ["Tidak", "Ya"])
    sex_opt = st.selectbox("Jenis Kelamin", ["Perempuan", "Laki-laki"])

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. Eksekusi Prediksi & Rekomendasi
# ---------------------------------------------------------
def get_binary_val(val_str):
    return 1.0 if val_str in ["Ya", "Laki-laki"] else 0.0


raw_input = {
    "HighBP": get_binary_val(highbp_opt),
    "HighChol": get_binary_val(highchol_opt),
    "CholCheck": get_binary_val(cholcheck_opt),
    "BMI": float(bmi),
    "Smoker": get_binary_val(smoker_opt),
    "Stroke": 0.0,
    "HeartDiseaseorAttack": get_binary_val(heartdisease_opt),
    "PhysActivity": 1.0,
    "Fruits": 1.0,
    "Veggies": 1.0,
    "HvyAlcoholConsump": 0.0,
    "AnyHealthcare": 1.0,
    "NoDocbcCost": 0.0,
    "GenHlth": float(genhlth),
    "MentHlth": 0.0,
    "PhysHlth": float(physhlth),
    "DiffWalk": 0.0,
    "Sex": get_binary_val(sex_opt),
    "Age": age_val,
    "Education": 4.0,
    "Income": 5.0,
}

input_df = pd.DataFrame([raw_input])

if hasattr(diabetes_model, "feature_names_in_"):
    model_cols = list(diabetes_model.feature_names_in_)
    if model_cols[0].islower():
        input_df.columns = [c.lower() for c in input_df.columns]
        input_df = input_df.reindex(columns=model_cols, fill_value=0.0)
    else:
        input_df = input_df.reindex(columns=model_cols, fill_value=0.0)

if st.button("Analisis Kesehatan & Rekomendasi Menu", use_container_width=True):
    if hasattr(diabetes_model, "predict_proba"):
        probs = diabetes_model.predict_proba(input_df)[0]
        if len(probs) > 2 and probs[2] >= 0.25:
            prediction = 2
        elif probs[1] >= 0.18:
            prediction = 1
        else:
            prediction = int(np.argmax(probs))
    else:
        raw_pred = diabetes_model.predict(input_df)[0]
        prediction = 2 if raw_pred == 1 else raw_pred

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">📊 Hasil Analisis Ringkas</div>', unsafe_allow_html=True)

    if prediction == 0:
        st.success("🟢 **Bebas Diabetes / Sehat**\n\nIndikator kesehatan berada di batas normal. Tetap pertahankan pola hidup sehat.")
    elif prediction == 1:
        st.warning("🟡 **Terindikasi Prediabetes**\n\nTerdeteksi risiko sedang. Disarankan untuk membatasi asupan karbohidrat dan gula.")
    else:
        st.error("🔴 **Risiko Tinggi Diabetes**\n\nIndikator kesehatan menunjukkan potensi risiko tinggi. Disarankan untuk konsultasi ke medis.")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">🥗 Rekomendasi Menu Kuliner Seimbang</div>', unsafe_allow_html=True)

    try:
        filtered_foods = foods_df.copy()

        for col in ['calories_kcal', 'carbohydrate_g', 'fat_g', 'proteins_g']:
            if col in filtered_foods.columns:
                filtered_foods[col] = pd.to_numeric(filtered_foods[col], errors='coerce')

        if prediction == 2:
            candidate_foods = filtered_foods[
                (filtered_foods['carbohydrate_g'] <= 15) & 
                (filtered_foods['calories_kcal'] <= 250)
            ]
        elif prediction == 1:
            candidate_foods = filtered_foods[
                (filtered_foods['carbohydrate_g'] <= 30) & 
                (filtered_foods['calories_kcal'] <= 350)
            ]
        else:
            candidate_foods = filtered_foods[
                (filtered_foods['calories_kcal'] <= 500) & 
                (filtered_foods['carbohydrate_g'] <= 60)
            ]

        if len(candidate_foods) >= 5:
            recommendations = candidate_foods.sample(5)
        elif not candidate_foods.empty:
            recommendations = candidate_foods
        else:
            recommendations = filtered_foods.sort_values(by=['carbohydrate_g'], ascending=True).head(5)

        # RENDER TABEL MENGGUNAKAN HTML CONTAINER BIAR Wajib Terang
        html_table = recommendations.to_html(classes="custom-table", index=False)
        st.markdown(f'<div class="table-container">{html_table}</div>', unsafe_allow_html=True)

    except Exception as err:
        st.error(f"Gagal memproses rekomendasi makanan: {err}")