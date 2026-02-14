import pandas as pd
import streamlit as st
import plotly.express as px

# =============================
# KONFIGURASI AWAL
# =============================
st.set_page_config(page_title="Dashboard Kuesioner|By:Jose Napitupulu",
                    layout="wide",
                    page_icon="📊")

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

color_map = {
    "SS": "#2ecc71",
    "S": "#27ae60",
    "CS": "#f1c40f",
    "CTS": "#e67e22",
    "TS": "#e74c3c",
    "STS": "#c0392b"
}

# =============================
# PREPROCESS DATA
# =============================
all_answers = df.melt(var_name="Pertanyaan", value_name="Jawaban")
all_answers["Skor"] = all_answers["Jawaban"].map(score_map)
all_answers["Kategori"] = all_answers["Jawaban"].map(category_map)

# =============================
# DISTRIBUSI JAWABAN KESELURUHAN
# =============================
order_skala = ["SS", "S", "CS", "CTS", "TS", "STS"]

dist_all = (
    all_answers["Jawaban"]
    .value_counts()
    .reindex(order_skala)
    .reset_index()
)

dist_all.columns = ["Jawaban", "Jumlah"]

dist_all["Persen"] = (
    dist_all["Jumlah"] / dist_all["Jumlah"].sum() * 100
).round(1)


# =============================
# RATA-RATA SKOR
# =============================
mean_score = (
    all_answers
    .groupby("Pertanyaan")["Skor"]
    .mean()
    .reset_index()
)


# =============================
# DISTRIBUSI KATEGORI
# =============================
category_dist = (
    all_answers["Kategori"]
    .value_counts()
    .reset_index()
)

category_dist.columns = ["Kategori", "Jumlah"]
# =============================
# JUDUL
# =============================
st.title("📊 Dashboard Visualisasi Data Kuesioner")
col1, col2 = st.columns(2)

total_respon = len(all_answers)
avg_score = round(all_answers["Skor"].mean(), 2)

positif_pct = round(
    (all_answers["Kategori"] == "Positif").mean() * 100, 1
)

negatif_pct = round(
    (all_answers["Kategori"] == "Negatif").mean() * 100, 1
)

k1, k2, k3, k4 = st.columns(4)

k1.metric("Total Respon", total_respon)
k2.metric("Rata-rata Skor", avg_score)
k3.metric("Positif (%)", positif_pct)
k4.metric("Negatif (%)", negatif_pct)

st.sidebar.markdown("""
<div style="font-size:20px; font-weight:600;">
📊 Data Kuesioner
</div>
<hr style="margin-top:6px; margin-bottom:12px;">
""", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "Pilih Halaman",
    ["Dashboard", "Hasil Analisis"]
)



st.sidebar.markdown("""

<style>
                    

/* box profile */
.profile-box {
    padding: 12px 16px;
    border-radius: 10px;
    background: #1f2937;
    margin-top: 10px;
    animation: glow 3s infinite alternate;
}

.profile-title {
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 6px;
}

.profile-item {
    font-size: 0.95rem;
    margin: 2px 0;
}

/* link github */
.profile-item a {
    color: #3b82f6;
    text-decoration: none;
}

.profile-item a:hover {
    text-decoration: underline;
}

/* glow animation */
@keyframes glow {
    from { box-shadow: 0 0 5px rgba(59,130,246,0.4); }
    to   { box-shadow: 0 0 14px rgba(59,130,246,0.8); }
}

</style>


<div class="profile-box">
    <div class="profile-title">👤 Profile</div>
    <div class="profile-item">Jose Napitupulu</div>
    <div class="profile-item">
        <a href="https://github.com/JoseNapitupulu" target="_blank">GitHub</a>
    </div>
</div>
""", unsafe_allow_html=True)


if menu == "Dashboard":
    # =============================
    # 1. BAR CHART DISTRIBUSI JAWABAN
    # =============================
    with col1:
        st.subheader("Distribusi Jawaban Kuesioner")
        

        # urutan skala yang benar
        order_skala = ["SS", "S", "CS", "CTS", "TS", "STS"]

        dist_all = (
            all_answers["Jawaban"]
            .value_counts()
            .reindex(order_skala)
            .reset_index()
        )

        dist_all.columns = ["Jawaban", "Jumlah"]

        # hitung persen
        dist_all["Persen"] = (
            dist_all["Jumlah"] / dist_all["Jumlah"].sum() * 100
        ).round(1)

        fig1 = px.bar(
            dist_all,
            x="Jawaban",
            y="Jumlah",
            text="Jumlah",
            color="Jawaban",
            title="Distribusi Jawaban Kuesioner"
        )

        fig1.update_traces(textposition="outside")

        fig1.update_layout(
            xaxis_title="Skala Jawaban",
            yaxis_title="Jumlah",
            showlegend=False,
            uniformtext_minsize=10,
            uniformtext_mode="hide"
        )
        st.plotly_chart(fig1, use_container_width=True)


    # =============================
    # 2. PIE CHART PROPORSI JAWABAN
    # =============================
    with col2:
        st.subheader("Proporsi Jawaban")
        

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
    
    col3, col4 = st.columns(2)

    with col3:
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
    with col4:
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
    col5, col6 = st.columns(2)

    with col5:
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
    with col6:
        st.subheader("Heatmap Rata-rata Skor")

        heatmap_data = mean_score.set_index("Pertanyaan")

        fig6 = px.imshow(
            heatmap_data.T,
            text_auto=True,
            aspect="auto",
            title="Heatmap Rata-rata Skor per Pertanyaan"
        )
        st.plotly_chart(fig6, use_container_width=True)
    
elif menu == "Hasil Analisis":
    st.header("Hasil Analisis Kuesioner")

    left, right = st.columns([1,2])
    with left:
        target_question = st.selectbox(
            "Pilih Analisis",
            [
                "q1","q2","q3","q4","q5","q6",
                "q7","q8","q9","q10","q11","q12","q13"
            ]
        )

    with right:
            if target_question == "q1":

                st.success("CS | 500 | 70.1")

                fig = px.bar(
                    dist_all,
                    x="Jawaban",
                    y="Jumlah",
                    color="Jawaban",
                    title="Distribusi Jawaban Keseluruhan"
                )
                st.plotly_chart(fig, width="stretch")


            elif target_question == "q2":

                st.success("STS | 4 | 0.2")

                fig = px.bar(
                    dist_all,
                    x="Jawaban",
                    y="Jumlah",
                    color="Jawaban",
                    title="Distribusi Jawaban Keseluruhan"
                )
                st.plotly_chart(fig, width="stretch")


            elif target_question == "q3":

                st.success("Q9 | 21 | 18.6")

                ss_data = (
                    all_answers[all_answers["Jawaban"] == "SS"]
                    .groupby("Pertanyaan")
                    .size()
                    .reset_index(name="Jumlah")
                )

                fig = px.bar(
                    ss_data,
                    x="Pertanyaan",
                    y="Jumlah",
                    title="Distribusi SS per Pertanyaan"
                )
                st.plotly_chart(fig, width="stretch")


            elif target_question == "q4":

                st.success("Q16 | 75 | 66.4")

                s_data = (
                    all_answers[all_answers["Jawaban"] == "S"]
                    .groupby("Pertanyaan")
                    .size()
                    .reset_index(name="Jumlah")
                )

                fig = px.bar(
                    s_data,
                    x="Pertanyaan",
                    y="Jumlah",
                    title="Distribusi S per Pertanyaan"
                )
                st.plotly_chart(fig, width="stretch")


            elif target_question == "q5":

                st.success("Q2 | 36 | 31.9")

                cs_data = (
                    all_answers[all_answers["Jawaban"] == "CS"]
                    .groupby("Pertanyaan")
                    .size()
                    .reset_index(name="Jumlah")
                )

                fig = px.bar(
                    cs_data,
                    x="Pertanyaan",
                    y="Jumlah",
                    title="Distribusi CS per Pertanyaan"
                )
                st.plotly_chart(fig, width="stretch")


            elif target_question == "q6":

                st.success("Q9 | 8 | 7.1")

                cts_data = (
                    all_answers[all_answers["Jawaban"] == "CTS"]
                    .groupby("Pertanyaan")
                    .size()
                    .reset_index(name="Jumlah")
                )

                fig = px.bar(
                    cts_data,
                    x="Pertanyaan",
                    y="Jumlah",
                    title="Distribusi CTS per Pertanyaan"
                )
                st.plotly_chart(fig, width="stretch")


            elif target_question == "q7":

                st.success("Q12 | 3 | 2.7")

                ts_data = (
                    all_answers[all_answers["Jawaban"] == "TS"]
                    .groupby("Pertanyaan")
                    .size()
                    .reset_index(name="Jumlah")
                )

                fig = px.bar(
                    ts_data,
                    x="Pertanyaan",
                    y="Jumlah",
                    title="Distribusi TS per Pertanyaan"
                )
                st.plotly_chart(fig, width="stretch")


            elif target_question == "q8":

                st.success("Q12 | 3 | 2.7")

                ts_data = (
                    all_answers[all_answers["Jawaban"] == "TS"]
                    .groupby("Pertanyaan")
                    .size()
                    .reset_index(name="Jumlah")
                )

                fig = px.bar(
                    ts_data,
                    x="Pertanyaan",
                    y="Jumlah",
                    title="Distribusi TS per Pertanyaan"
                )
                st.plotly_chart(fig, width="stretch")


            elif target_question == "q9":

                st.success("Q1:0.9 | Q2:0.9 | Q9:0.9 | Q11:0.9")

                sts_data = (
                    all_answers[all_answers["Jawaban"] == "STS"]
                    .groupby("Pertanyaan")
                    .size()
                    .reset_index(name="Jumlah")
                )

                fig = px.bar(
                    sts_data,
                    x="Pertanyaan",
                    y="Jumlah",
                    title="Distribusi STS per Pertanyaan"
                )
                st.plotly_chart(fig, width="stretch")


            elif target_question == "q10":

                st.success("4.80")

                fig = px.bar(
                    mean_score,
                    x="Pertanyaan",
                    y="Skor",
                    title="Rata-rata Skor per Pertanyaan"
                )
                st.plotly_chart(fig, width="stretch")


            elif target_question == "q11":

                st.success("Q5:4.95")

                fig = px.bar(
                    mean_score.sort_values("Skor", ascending=False),
                    x="Pertanyaan",
                    y="Skor",
                    title="Ranking Skor Rata-rata"
                )
                st.plotly_chart(fig, width="stretch")


            elif target_question == "q12":

                st.success("Q12:4.59")

                fig = px.bar(
                    mean_score.sort_values("Skor"),
                    x="Pertanyaan",
                    y="Skor",
                    title="Ranking Skor Terendah"
                )
                st.plotly_chart(fig, width="stretch")


            elif target_question == "q13":

                st.success("positif=1396:72.7 | netral=471:24.5 | negatif=54:2.8")

                fig = px.pie(
                    category_dist,
                    names="Kategori",
                    values="Jumlah",
                    title="Distribusi Kategori Jawaban"
                )
                st.plotly_chart(fig, width="stretch")


st.markdown(
    """
    <hr style="margin-top:30px;">
    <div style='text-align:center; font-size:14px; color:gray;'>
        © 2025 Jose Napitupulu — Dashboard Visualisasi Data Kuesioner
    </div>
    """,
    unsafe_allow_html=True
) 



