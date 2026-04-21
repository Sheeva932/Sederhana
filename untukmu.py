import streamlit as st
import pandas as pd

st.set_page_config(page_title="FilmFeel", page_icon="🎬", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background-color: #080808;
    color: #e0e0e0;
}

/* Hide default streamlit elements */
#MainMenu, footer, header { visibility: hidden; }

.logo {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 3rem;
    letter-spacing: 6px;
    color: #fff;
    line-height: 1;
    margin-bottom: 4px;
}
.logo span { color: #c0392b; }
.tagline {
    font-size: 11px;
    letter-spacing: 3px;
    color: #444;
    text-transform: uppercase;
    margin-bottom: 2rem;
}
.section-label {
    font-size: 10px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #555;
    margin-bottom: 8px;
}
.film-card {
    background: #0f0f0f;
    border: 1px solid #1e1e1e;
    border-radius: 10px;
    padding: 16px 18px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 16px;
    transition: border-color 0.15s;
}
.film-card:hover { border-color: #252525; }
.film-number {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.6rem;
    color: #1e1e1e;
    min-width: 32px;
    text-align: right;
}
.film-title {
    font-size: 15px;
    font-weight: 500;
    color: #e8e8e8;
    margin: 0 0 4px 0;
}
.film-meta { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }
.genre-tag {
    font-size: 11px;
    letter-spacing: 1px;
    color: #555;
    text-transform: uppercase;
}
.mood-tag {
    font-size: 11px;
    background: #161616;
    border: 1px solid #1e1e1e;
    color: #444;
    padding: 2px 8px;
    border-radius: 4px;
}
.results-header {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    margin-bottom: 1rem;
}
.results-count {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.3rem;
    letter-spacing: 2px;
    color: #fff;
}
.results-filter {
    font-size: 11px;
    letter-spacing: 2px;
    color: #444;
    text-transform: uppercase;
}
.empty-state {
    text-align: center;
    padding: 3rem 0;
    color: #333;
    font-size: 12px;
    letter-spacing: 2px;
    text-transform: uppercase;
}
.divider {
    border: none;
    border-top: 1px solid #151515;
    margin: 2rem 0;
}
.strip {
    display: flex;
    gap: 4px;
    overflow: hidden;
    margin: 1.5rem 0;
}
.strip-hole {
    width: 18px;
    height: 10px;
    background: #151515;
    border-radius: 2px;
    flex-shrink: 0;
    display: inline-block;
}

/* Streamlit widget overrides */
div[data-baseweb="select"] > div {
    background-color: #111 !important;
    border-color: #1e1e1e !important;
    color: #e0e0e0 !important;
    border-radius: 8px !important;
}
div[data-baseweb="select"] span { color: #e0e0e0 !important; }
div[data-baseweb="popover"] { background: #111 !important; }
li[role="option"] { background: #111 !important; color: #e0e0e0 !important; }
li[role="option"]:hover { background: #1a1a1a !important; }

.stButton > button {
    background-color: #c0392b !important;
    color: #fff !important;
    border: none !important;
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 1.1rem !important;
    letter-spacing: 4px !important;
    padding: 0.75rem 1.5rem !important;
    border-radius: 8px !important;
    width: 100% !important;
    transition: background 0.2s !important;
}
.stButton > button:hover { background-color: #a93226 !important; }
</style>
""", unsafe_allow_html=True)

# --- DATA ---
data = pd.DataFrame([
    {"judul": "The Hangover",               "genre": "Comedy",          "mood": "Ringan",       "cocok": "Butuh Ketawa"},
    {"judul": "Rough Night",                "genre": "Comedy",          "mood": "Ringan",       "cocok": "Butuh Ketawa"},
    {"judul": "Spy",                        "genre": "Comedy, Action",  "mood": "Ringan",       "cocok": "Butuh Ketawa"},
    {"judul": "Scent of A Woman",           "genre": "Drama",           "mood": "Sedih",        "cocok": "Ingin Merasakan Sesuatu"},
    {"judul": "Coda",                       "genre": "Drama",           "mood": "Heartwarming", "cocok": "Butuh Motivasi"},
    {"judul": "Forrest Gump",               "genre": "Komedi Drama",    "mood": "Heartwarming", "cocok": "Overthinking"},
    {"judul": "The Green Book",             "genre": "Drama",           "mood": "Heartwarming", "cocok": "Butuh Inspirasi"},
    {"judul": "The Green Mile",             "genre": "Drama",           "mood": "Sedih",        "cocok": "Reflektif"},
    {"judul": "Titanic",                    "genre": "Drama",           "mood": "Sedih",        "cocok": "Butuh Tontonan Cinta"},
    {"judul": "One Piece Live Action",      "genre": "Petualangan",     "mood": "Ceria",        "cocok": "Butuh Mood Booster"},
    {"judul": "Game of Thrones",            "genre": "Drama",           "mood": "Menegangkan",  "cocok": "Butuh Naikkan Adrenalin"},
    {"judul": "The Knight of The Seven Kingdom", "genre": "Drama",      "mood": "Menegangkan",  "cocok": "Butuh Naikkan Adrenalin"},
    {"judul": "Conjuring",                  "genre": "Horror",          "mood": "Menegangkan",  "cocok": "Butuh Naikkan Adrenalin"},
    {"judul": "Dead Poets Society",         "genre": "Drama",           "mood": "Heartwarming", "cocok": "Butuh Inspirasi"},
    {"judul": "The Greatest Showman",       "genre": "Musikal",         "mood": "Heartwarming", "cocok": "Butuh Motivasi"},
    {"judul": "Frozen",                     "genre": "Musikal",         "mood": "Heartwarming", "cocok": "Butuh Motivasi"},
    {"judul": "Coco",                       "genre": "Fantasi",         "mood": "Sedih",        "cocok": "Ingin Merasakan Sesuatu"},
    {"judul": "Moana",                      "genre": "Petualangan",     "mood": "Ceria",        "cocok": "Butuh Motivasi"},
    {"judul": "Insidious",                  "genre": "Horor",           "mood": "Menegangkan",  "cocok": "Butuh Naikkan Adrenalin"},
    {"judul": "A Star is Born",             "genre": "Musikal",         "mood": "Sedih",        "cocok": "Ingin Merasakan Sesuatu"},
])

# --- HEADER ---
st.markdown('<div class="logo">Film<span>Feel</span></div>', unsafe_allow_html=True)
st.markdown('<div class="tagline">Temukan film yang tepat buat harimu</div>', unsafe_allow_html=True)
st.markdown('<div class="strip">' + '<div class="strip-hole"></div>' * 35 + '</div>', unsafe_allow_html=True)

# --- MOOD SELECTOR ---
st.markdown('<div class="section-label">Mood kamu sekarang</div>', unsafe_allow_html=True)
mood_emoji = {
    "Ringan": "😄 Ringan",
    "Sedih": "😢 Sedih",
    "Heartwarming": "🤍 Heartwarming",
    "Ceria": "✨ Ceria",
    "Menegangkan": "⚡ Menegangkan",
}
moods = data["mood"].unique().tolist()
mood_labels = [mood_emoji.get(m, m) for m in moods]

cols = st.columns(len(moods))
selected_mood = st.session_state.get("selected_mood", None)

for i, (col, mood, label) in enumerate(zip(cols, moods, mood_labels)):
    with col:
        if st.button(label, key=f"mood_{mood}"):
            st.session_state["selected_mood"] = mood
            st.session_state["selected_cocok"] = None
            st.rerun()

selected_mood = st.session_state.get("selected_mood", None)

# --- KEBUTUHAN SELECTOR ---
st.markdown('<br><div class="section-label">Kamu lagi butuh</div>', unsafe_allow_html=True)

if selected_mood:
    cocok_options = ["— Pilih kebutuhan —"] + data[data["mood"] == selected_mood]["cocok"].unique().tolist()
else:
    cocok_options = ["— Pilih mood dulu —"]

selected_cocok = st.selectbox("", cocok_options, label_visibility="collapsed")

# --- SEARCH BUTTON ---
st.markdown("<br>", unsafe_allow_html=True)
cari = st.button("🎬  TEMUKAN FILM")

# --- RESULTS ---
if cari:
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    if not selected_mood:
        st.markdown('<div class="empty-state">Pilih mood kamu dulu</div>', unsafe_allow_html=True)
    elif selected_cocok == "— Pilih kebutuhan —" or selected_cocok == "— Pilih mood dulu —":
        st.markdown('<div class="empty-state">Pilih kebutuhan kamu dulu</div>', unsafe_allow_html=True)
    else:
        hasil = data[(data["mood"] == selected_mood) & (data["cocok"] == selected_cocok)]

        if hasil.empty:
            st.markdown('<div class="empty-state">😶 Belum ada yang pas... coba pilih opsi lain</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'''
                <div class="results-header">
                    <span class="results-count">{len(hasil)} Film Untukmu</span>
                    <span class="results-filter">{selected_mood} · {selected_cocok}</span>
                </div>
            ''', unsafe_allow_html=True)

            for i, (_, row) in enumerate(hasil.iterrows(), 1):
                st.markdown(f'''
                    <div class="film-card">
                        <div style="flex:1">
                            <p class="film-title">{row["judul"]}</p>
                            <div class="film-meta">
                                <span class="genre-tag">{row["genre"]}</span>
                                <span class="mood-tag">{row["cocok"]}</span>
                            </div>
                        </div>
                        <span class="film-number">0{i}</span>
                    </div>
                ''', unsafe_allow_html=True)
