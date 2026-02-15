import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Dashboard Analisis Kuesioner", layout="wide")

st.title("📊 Dashboard Analisis Data Kuesioner")

# ===============================
# Upload File
# ===============================
uploaded_file = st.file_uploader("Upload File Excel Kuesioner", type=["xlsx"])

if uploaded_file is not None:

    df = pd.read_excel(uploaded_file)

    st.subheader("Preview Data")
    st.dataframe(df.head())

    # ===============================
    # Mapping Skor
    # ===============================
    skor_map = {
        "SS": 6,
        "S": 5,
        "CS": 4,
        "CTS": 3,
        "TS": 2,
        "STS": 1
    }

    kategori_map = {
        "SS": "Positif",
        "S": "Positif",
        "CS": "Netral",
        "CTS": "Negatif",
        "TS": "Negatif",
        "STS": "Negatif"
    }

    # ===============================
    # 1. Bar Chart Distribusi Keseluruhan
    # ===============================
    st.subheader("1️⃣ Distribusi Jawaban Keseluruhan")

    all_values = df.values.flatten()
    distribusi = pd.Series(all_values).value_counts().reset_index()
    distribusi.columns = ["Jawaban", "Jumlah"]

    fig1 = px.bar(distribusi, x="Jawaban", y="Jumlah",
                  color="Jawaban",
                  title="Distribusi Jawaban Keseluruhan")
    st.plotly_chart(fig1, use_container_width=True)

    # ===============================
    # 2. Pie Chart Proporsi
    # ===============================
    st.subheader("2️⃣ Proporsi Jawaban Keseluruhan")

    fig2 = px.pie(distribusi,
                  names="Jawaban",
                  values="Jumlah",
                  title="Proporsi Jawaban")
    st.plotly_chart(fig2, use_container_width=True)

    # ===============================
    # 3. Stacked Bar per Pertanyaan
    # ===============================
    st.subheader("3️⃣ Distribusi Jawaban per Pertanyaan")

    df_melt = df.melt(var_name="Pertanyaan", value_name="Jawaban")

    distribusi_per_pertanyaan = pd.crosstab(
        df_melt["Pertanyaan"],
        df_melt["Jawaban"]
    )

    fig3 = px.bar(distribusi_per_pertanyaan,
                  barmode="stack",
                  title="Distribusi Jawaban per Pertanyaan")
    st.plotly_chart(fig3, use_container_width=True)

    # ===============================
    # 4. Rata-rata Skor per Pertanyaan
    # ===============================
    st.subheader("4️⃣ Rata-rata Skor per Pertanyaan")

    df_skor = df.replace(skor_map)
    rata_rata = df_skor.mean().reset_index()
    rata_rata.columns = ["Pertanyaan", "Rata-rata Skor"]

    fig4 = px.bar(rata_rata,
                  x="Pertanyaan",
                  y="Rata-rata Skor",
                  color="Rata-rata Skor",
                  title="Rata-rata Skor per Pertanyaan")
    st.plotly_chart(fig4, use_container_width=True)

    # ===============================
    # 5. Kategori Positif / Netral / Negatif
    # ===============================
    st.subheader("5️⃣ Distribusi Kategori Jawaban")

    kategori = pd.Series(all_values).map(kategori_map)
    distribusi_kategori = kategori.value_counts().reset_index()
    distribusi_kategori.columns = ["Kategori", "Jumlah"]

    fig5 = px.bar(distribusi_kategori,
                  x="Kategori",
                  y="Jumlah",
                  color="Kategori",
                  title="Distribusi Kategori Jawaban")
    st.plotly_chart(fig5, use_container_width=True)

    # ===============================
    # BONUS 1: Heatmap
    # ===============================
    st.subheader("🎁 Bonus: Heatmap Distribusi Jawaban")

    heatmap_data = distribusi_per_pertanyaan.fillna(0)

    fig6 = go.Figure(data=go.Heatmap(
        z=heatmap_data.values,
        x=heatmap_data.columns,
        y=heatmap_data.index,
        colorscale="Blues"
    ))

    fig6.update_layout(title="Heatmap Distribusi Jawaban per Pertanyaan")
    st.plotly_chart(fig6, use_container_width=True)

    # ===============================
    # BONUS 2: Boxplot
    # ===============================
    st.subheader("🎁 Bonus: Boxplot Sebaran Skor")

    df_skor_melt = df_skor.melt(var_name="Pertanyaan", value_name="Skor")

    fig7 = px.box(df_skor_melt,
                  x="Pertanyaan",
                  y="Skor",
                  title="Sebaran Skor per Pertanyaan")
    st.plotly_chart(fig7, use_container_width=True)

else:
    st.warning("Silakan upload file Excel terlebih dahulu.")