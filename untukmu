import streamlit as st
import pandas as pd

# Load data
data = pd.read_csv("data.csv")

st.title("🎬 Rekomendasi Film Berdasarkan Perasaan Kamu")

# Pertanyaan ke user
mood_user = st.selectbox(
    "Mood kamu sekarang:",
    data["Mood"].unique()
)

kebutuhan_user = st.selectbox(
    "Kamu lagi butuh:",
    data["Cocok Saat"].unique()
)

# Logic
if st.button("Cari Rekomendasi"):
    hasil = data[
        (data["Mood"] == mood_user) &
        (data["Cocok Saat"] == kebutuhan_user)
    ]

    if not hasil.empty:
        st.subheader("✨ Ini rekomendasi buat kamu:")
        for i, row in hasil.iterrows():
            st.write(f"🎥 {row['Judul']} ({row['Genre']})")
    else:
        st.write("Belum ada yang pas banget... coba pilih opsi lain ya")
