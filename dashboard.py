import pandas as pd
import streamlit as st
import plotly.express as px

# =============================
# KONFIGURASI AWAL
# =============================
st.set_page_config(page_title="Dashboard Kuesioner", layout="wide")

FILE_PATH = r"C:\Users\LENOVO\OneDrive\Documents\pemodelan dan simulasi\modsim-2026-p2-ifs25026-latihan\data_kuesioner.xlsx"

# =============================
# LOAD DATA
# =============================
df = pd.read_excel(FILE_PATH)

questions = df.columns.tolist()

# =============================
# MAPPING SKOR
# =============================
score_map = {
    "SS": 6,
    "S": 5,
    "CS": 4,
    "CTS": 3,
    "TS": 2,
    "STS": 1
}

category_map = {
    "SS": "Positif",
    "S": "Positif",
    "CS": "Netral",
    "CTS": "Negatif",
    "TS": "Negatif",
    "STS": "Negatif"
}

# =============================
# PREPROCESS DATA
# =============================
all_answers = df.melt(var_name="Pertanyaan", value_name="Jawaban")
all_answers["Skor"] = all_answers["Jawaban"].map(score_map)
all_answers["Kategori"] = all_answers["Jawaban"].map(category_map)

# =============================
# JUDUL
# =============================
st.title("📊 Dashboard Visualisasi Data Kuesioner")

# =============================
# 1. BAR CHART DISTRIBUSI JAWABAN
# =============================
st.subheader("Distribusi Jawaban Kuesioner (Keseluruhan)")

dist_all = (
    all_answers["Jawaban"]
    .value_counts()
    .reset_index()
)

dist_all.columns = ["Jawaban", "Jumlah"]

fig1 = px.bar(
    dist_all,
    x="Jawaban",
    y="Jumlah",
    title="Distribusi Jawaban Kuesioner",
    text="Jumlah"
)


fig1 = px.bar(
    dist_all,
    x="Jawaban",
    y="Jumlah",
    text="Jumlah",
    title="Distribusi Jawaban"
)
st.plotly_chart(fig1, use_container_width=True)

# =============================
# 2. PIE CHART PROPORSI JAWABAN
# =============================
st.subheader("Proporsi Jawaban Kuesioner")

fig2 = px.pie(
    dist_all,
    names="Jawaban",
    values="Jumlah",
    title="Proporsi Jawaban"
)
st.plotly_chart(fig2, use_container_width=True)

# =============================
# 3. STACKED BAR PER PERTANYAAN
# =============================
st.subheader("Distribusi Jawaban per Pertanyaan")

stacked = (
    all_answers
    .groupby(["Pertanyaan", "Jawaban"])
    .size()
    .reset_index(name="Jumlah")
)

fig3 = px.bar(
    stacked,
    x="Pertanyaan",
    y="Jumlah",
    color="Jawaban",
    title="Stacked Bar Distribusi Jawaban per Pertanyaan"
)
st.plotly_chart(fig3, use_container_width=True)

# =============================
# 4. BAR CHART RATA-RATA SKOR
# =============================
st.subheader("Rata-rata Skor per Pertanyaan")

mean_score = (
    all_answers
    .groupby("Pertanyaan")["Skor"]
    .mean()
    .reset_index()
)

fig4 = px.bar(
    mean_score,
    x="Pertanyaan",
    y="Skor",
    text=mean_score["Skor"].round(2),
    title="Rata-rata Skor per Pertanyaan"
)
st.plotly_chart(fig4, use_container_width=True)

# =============================
# 5. DISTRIBUSI KATEGORI POSITIF / NETRAL / NEGATIF
# =============================
st.subheader("Distribusi Kategori Jawaban")

category_dist = (
    all_answers["Kategori"]
    .value_counts()
    .reset_index()
)
category_dist.columns = ["Kategori", "Jumlah"]

fig5 = px.bar(
    category_dist,
    x="Kategori",
    y="Jumlah",
    text="Jumlah",
    title="Distribusi Kategori Jawaban"
)
st.plotly_chart(fig5, use_container_width=True)

# =============================
# 6. BONUS: HEATMAP SKOR RATA-RATA
# =============================
st.subheader("Bonus: Heatmap Rata-rata Skor")

heatmap_data = mean_score.set_index("Pertanyaan")

fig6 = px.imshow(
    heatmap_data.T,
    text_auto=True,
    aspect="auto",
    title="Heatmap Rata-rata Skor per Pertanyaan"
)
st.plotly_chart(fig6, use_container_width=True)
