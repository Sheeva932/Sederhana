<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FilmFeel — Rekomendasi Berdasarkan Mood</title>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: #080808;
    color: #e0e0e0;
    font-family: 'DM Sans', sans-serif;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 3rem 1.5rem 4rem;
  }

  .container {
    width: 100%;
    max-width: 680px;
  }

  /* Header */
  .header { margin-bottom: 2.5rem; }
  .logo {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 3rem;
    letter-spacing: 6px;
    color: #fff;
    line-height: 1;
  }
  .logo span { color: #c0392b; }
  .tagline {
    font-size: 11px;
    letter-spacing: 3.5px;
    color: #444;
    text-transform: uppercase;
    margin-top: 6px;
  }

  /* Film strip decoration */
  .strip {
    display: flex;
    gap: 4px;
    margin: 1.5rem 0;
    overflow: hidden;
  }
  .strip-hole {
    width: 18px;
    height: 10px;
    background: #151515;
    border-radius: 2px;
    flex-shrink: 0;
  }

  /* Section label */
  .section-label {
    font-size: 10px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #444;
    margin-bottom: 10px;
  }

  /* Mood grid */
  .mood-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
    gap: 8px;
    margin-bottom: 2rem;
  }
  .mood-btn {
    background: #111;
    border: 1px solid #1e1e1e;
    color: #888;
    padding: 10px 12px;
    border-radius: 8px;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    cursor: pointer;
    text-align: left;
    transition: all 0.15s;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .mood-btn:hover { border-color: #333; color: #ccc; background: #131313; }
  .mood-btn.active {
    background: #1a1a1a;
    border-color: #c0392b;
    color: #fff;
  }
  .mood-btn .mood-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #2a2a2a;
    flex-shrink: 0;
    transition: background 0.15s;
  }
  .mood-btn.active .mood-dot { background: #c0392b; }

  /* Kebutuhan select */
  .select-wrapper {
    position: relative;
    margin-bottom: 2rem;
  }
  .select-wrapper select {
    width: 100%;
    background: #111;
    border: 1px solid #1e1e1e;
    color: #e0e0e0;
    padding: 13px 40px 13px 16px;
    border-radius: 8px;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    appearance: none;
    cursor: pointer;
    transition: border-color 0.15s;
  }
  .select-wrapper select:focus { outline: none; border-color: #333; }
  .select-arrow {
    position: absolute;
    right: 14px;
    top: 50%;
    transform: translateY(-50%);
    pointer-events: none;
    color: #444;
    font-size: 10px;
  }

  /* Search button */
  .search-btn {
    width: 100%;
    background: #c0392b;
    color: #fff;
    border: none;
    padding: 15px;
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.15rem;
    letter-spacing: 4px;
    cursor: pointer;
    border-radius: 8px;
    transition: background 0.2s, transform 0.1s;
  }
  .search-btn:hover { background: #a93226; }
  .search-btn:active { transform: scale(0.99); }

  /* Divider */
  .divider {
    border: none;
    border-top: 1px solid #151515;
    margin: 2.5rem 0;
  }

  /* Results */
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

  /* Film card */
  .film-card {
    background: #0f0f0f;
    border: 1px solid #181818;
    border-radius: 10px;
    padding: 16px 18px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 16px;
    transition: border-color 0.15s, background 0.15s;
    cursor: default;
  }
  .film-card:hover { border-color: #252525; background: #111; }

  .film-poster {
    width: 44px;
    height: 58px;
    background: #161616;
    border-radius: 5px;
    border: 1px solid #202020;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }
  .poster-top, .poster-bottom {
    display: flex;
    gap: 3px;
    padding: 4px 4px 2px;
  }
  .poster-hole {
    width: 5px;
    height: 4px;
    background: #0a0a0a;
    border-radius: 1px;
  }
  .poster-frame {
    flex: 1;
    background: #1e1e1e;
    margin: 0 4px;
    border-radius: 2px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .poster-line {
    width: 16px;
    height: 2px;
    background: #2a2a2a;
    border-radius: 1px;
  }

  .film-info { flex: 1; min-width: 0; }
  .film-title {
    font-size: 14px;
    font-weight: 500;
    color: #e8e8e8;
    margin-bottom: 4px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .film-meta {
    display: flex;
    gap: 8px;
    align-items: center;
    flex-wrap: wrap;
  }
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
    letter-spacing: 0.5px;
  }

  .film-number {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.4rem;
    color: #1e1e1e;
    letter-spacing: 1px;
    min-width: 28px;
    text-align: right;
  }

  /* Empty state */
  .empty-state {
    text-align: center;
    padding: 3rem 0;
  }
  .empty-icon {
    font-size: 2rem;
    margin-bottom: 1rem;
    opacity: 0.3;
  }
  .empty-text {
    color: #333;
    font-size: 13px;
    letter-spacing: 2px;
    text-transform: uppercase;
  }

  /* No selection state */
  .hint-text {
    text-align: center;
    padding: 2rem 0;
    color: #2a2a2a;
    font-size: 12px;
    letter-spacing: 2px;
    text-transform: uppercase;
  }

  /* Footer */
  .footer {
    margin-top: 3rem;
    text-align: center;
    font-size: 11px;
    letter-spacing: 2px;
    color: #222;
    text-transform: uppercase;
  }
</style>
</head>
<body>

<div class="container">

  <!-- Header -->
  <header class="header">
    <h1 class="logo">Film<span>Feel</span></h1>
    <p class="tagline">Temukan film yang tepat buat harimu</p>
  </header>

  <!-- Film strip deco -->
  <div class="strip" id="strip"></div>

  <!-- Mood selector -->
  <p class="section-label">Mood kamu sekarang</p>
  <div class="mood-grid" id="mood-grid"></div>

  <!-- Kebutuhan selector -->
  <p class="section-label">Kamu lagi butuh</p>
  <div class="select-wrapper">
    <select id="kebutuhan-select">
      <option value="">— Pilih kebutuhan —</option>
    </select>
    <span class="select-arrow">▼</span>
  </div>

  <!-- Search -->
  <button class="search-btn" onclick="cariFilm()">Temukan Film</button>

  <!-- Results -->
  <hr class="divider" id="results-divider" style="display:none">
  <div id="results-section" style="display:none">
    <div class="results-header">
      <span class="results-count" id="results-count"></span>
      <span class="results-filter" id="results-filter"></span>
    </div>
    <div id="film-list"></div>
  </div>

  <p class="footer">FilmFeel &mdash; Temukan tontonanmu</p>
</div>

<script>
  const data = [
    { judul: "The Hangover", genre: "Comedy", mood: "Ringan", cocok: "Butuh Ketawa" },
    { judul: "Rough Night", genre: "Comedy", mood: "Ringan", cocok: "Butuh Ketawa" },
    { judul: "Spy", genre: "Comedy, Action", mood: "Ringan", cocok: "Butuh Ketawa" },
    { judul: "Scent of A Woman", genre: "Drama", mood: "Sedih", cocok: "Ingin Merasakan Sesuatu" },
    { judul: "Coda", genre: "Drama", mood: "Heartwarming", cocok: "Butuh Motivasi" },
    { judul: "Forrest Gump", genre: "Komedi Drama", mood: "Heartwarming", cocok: "Overthinking" },
    { judul: "The Green Book", genre: "Drama", mood: "Heartwarming", cocok: "Butuh Inspirasi" },
    { judul: "The Green Mile", genre: "Drama", mood: "Sedih", cocok: "Reflektif" },
    { judul: "Titanic", genre: "Drama", mood: "Sedih", cocok: "Butuh Tontonan Cinta" },
    { judul: "One Piece Live Action", genre: "Petualangan", mood: "Ceria", cocok: "Butuh Mood Booster" },
    { judul: "Game of Thrones", genre: "Drama", mood: "Menegangkan", cocok: "Butuh Naikkan Adrenalin" },
    { judul: "The Knight of The Seven Kingdom", genre: "Drama", mood: "Menegangkan", cocok: "Butuh Naikkan Adrenalin" },
    { judul: "Conjuring", genre: "Horror", mood: "Menegangkan", cocok: "Butuh Naikkan Adrenalin" },
    { judul: "Dead Poets Society", genre: "Drama", mood: "Heartwarming", cocok: "Butuh Inspirasi" },
    { judul: "The Greatest Showman", genre: "Musikal", mood: "Heartwarming", cocok: "Butuh Motivasi" },
    { judul: "Frozen", genre: "Musikal", mood: "Heartwarming", cocok: "Butuh Motivasi" },
    { judul: "Coco", genre: "Fantasi", mood: "Sedih", cocok: "Ingin Merasakan Sesuatu" },
    { judul: "Moana", genre: "Petualangan", mood: "Ceria", cocok: "Butuh Motivasi" },
    { judul: "Insidious", genre: "Horor", mood: "Menegangkan", cocok: "Butuh Naikkan Adrenalin" },
    { judul: "A Star is Born", genre: "Musikal", mood: "Sedih", cocok: "Ingin Merasakan Sesuatu" }
  ];

  // Fix & normalize data
  data.forEach(d => {
    d.mood = d.mood.trim();
    d.cocok = d.cocok.trim();
  });

  let selectedMood = null;

  // Build film strip decoration
  const strip = document.getElementById('strip');
  for (let i = 0; i < 40; i++) {
    const hole = document.createElement('div');
    hole.className = 'strip-hole';
    strip.appendChild(hole);
  }

  // Build mood buttons
  const moods = [...new Set(data.map(d => d.mood))];
  const moodGrid = document.getElementById('mood-grid');
  const moodEmoji = {
    'Ringan': '😄', 'Sedih': '😢', 'Heartwarming': '🤍',
    'Ceria': '✨', 'Menegangkan': '⚡'
  };
  moods.forEach(m => {
    const btn = document.createElement('button');
    btn.className = 'mood-btn';
    btn.innerHTML = `<span class="mood-dot"></span>${moodEmoji[m] || '🎬'} ${m}`;
    btn.onclick = () => {
      document.querySelectorAll('.mood-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      selectedMood = m;
      updateKebutuhan(m);
    };
    moodGrid.appendChild(btn);
  });

  // Populate kebutuhan based on selected mood
  const kebutSel = document.getElementById('kebutuhan-select');
  function updateKebutuhan(mood) {
    const filtered = [...new Set(data.filter(d => d.mood === mood).map(d => d.cocok))];
    kebutSel.innerHTML = '<option value="">— Pilih kebutuhan —</option>';
    filtered.forEach(k => {
      const o = document.createElement('option');
      o.value = k;
      o.textContent = k;
      kebutSel.appendChild(o);
    });
  }

  function cariFilm() {
    const kebutuhan = kebutSel.value;
    const resultsSection = document.getElementById('results-section');
    const resultsDivider = document.getElementById('results-divider');
    const filmList = document.getElementById('film-list');
    const resultsCount = document.getElementById('results-count');
    const resultsFilter = document.getElementById('results-filter');

    resultsSection.style.display = 'block';
    resultsDivider.style.display = 'block';
    filmList.innerHTML = '';

    if (!selectedMood) {
      filmList.innerHTML = `<div class="hint-text">Pilih mood kamu dulu</div>`;
      resultsCount.textContent = '';
      resultsFilter.textContent = '';
      return;
    }

    const hasil = data.filter(d =>
      d.mood === selectedMood &&
      (!kebutuhan || d.cocok === kebutuhan)
    );

    if (hasil.length === 0) {
      resultsCount.textContent = 'Tidak Ditemukan';
      resultsFilter.textContent = '';
      filmList.innerHTML = `
        <div class="empty-state">
          <div class="empty-icon">🎞</div>
          <p class="empty-text">Belum ada film yang pas... coba pilih opsi lain</p>
        </div>`;
      return;
    }

    resultsCount.textContent = hasil.length + ' Film Untukmu';
    resultsFilter.textContent = selectedMood + (kebutuhan ? ' · ' + kebutuhan : '');

    hasil.forEach((f, i) => {
      filmList.innerHTML += `
        <div class="film-card">
          <div class="film-poster">
            <div class="poster-top">
              <div class="poster-hole"></div><div class="poster-hole"></div><div class="poster-hole"></div>
            </div>
            <div class="poster-frame"><div class="poster-line"></div></div>
            <div class="poster-bottom">
              <div class="poster-hole"></div><div class="poster-hole"></div><div class="poster-hole"></div>
            </div>
          </div>
          <div class="film-info">
            <p class="film-title">${f.judul}</p>
            <div class="film-meta">
              <span class="genre-tag">${f.genre}</span>
              <span class="mood-tag">${f.cocok}</span>
            </div>
          </div>
          <span class="film-number">0${i + 1}</span>
        </div>`;
    });
  }
</script>
</body>
</html>
