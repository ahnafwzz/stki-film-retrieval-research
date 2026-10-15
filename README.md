# CineMatch: Film Synopsis Retrieval System (Research Repository)

Repositori ini berisi tahapan riset komputasi dan eksperimen untuk **CineMatch**, sebuah purwarupa sistem temu balik informasi (*Information Retrieval*) yang menemukan judul film berdasarkan deskripsi alur cerita atau potongan ingatan adegan dalam bahasa alami.

Proyek ini merupakan pemenuhan Tugas Akhir Mata Kuliah STKI. Fokusnya adalah menguji penelusuran leksikal berbasis **Vector Space Model (VSM)** dengan pembobotan **TF-IDF** dan **Cosine Similarity**, serta menganalisis keterbatasannya.

> Repositori ini khusus untuk eksperimen dan dokumentasi riset. Kode aplikasi web (Streamlit) berada pada repositori terpisah, `cinematch-streamlit-app`.

## Status Pengerjaan

| Tahap | Kegiatan | Status |
|-------|----------|--------|
| 1 | Inisiasi proyek, dataset, dan EDA | ✅ Selesai |
| 2 | Modul `preprocess.py` (S1 sampai S4) | ⏳ Belum |
| 3 | 30 film target dan 30 kueri uji | ⏳ Belum |
| 4 | TF-IDF, cosine similarity, dan ranking | ⏳ Belum |
| 5 | Eksperimen S1 sampai S4 | ⏳ Belum |
| 6 | Analisis kegagalan dan ekspor model | ⏳ Belum |
| 7 | Aplikasi Streamlit (repo produk) | ⏳ Belum |
| 8 | Laporan akhir dan demo | ⏳ Belum |

Rincian per tahap ada di [weekly_log.md](weekly_log.md).

## Tujuan Eksperimen

1. Membandingkan empat skenario *text preprocessing* (S1: teks mentah sampai S4: stemming penuh) terhadap keberhasilan pencarian.
2. Mengevaluasi sistem dengan **Hit Rate@5** dan **Mean Reciprocal Rank (MRR)** pada 30 kueri uji.
3. Menganalisis batasan model leksikal, khususnya frekuensi kegagalan akibat *vocabulary mismatch*.

## Dataset

- **Sumber:** *TMDB 5000 Movie Dataset* di Kaggle (data asli berasal dari The Movie Database). Periksa ketentuan lisensi pada halaman dataset.
- **Subset:** 500 baris pertama sesuai urutan asli file (bukan sampel acak), dengan dua kolom: `title` dan `overview`.
- **File:** `dataset/movies_clean.csv`.

## Struktur Repositori

Tanda ✅ berarti sudah ada, ⏳ berarti direncanakan pada tahap berikutnya.

```text
stki-film-retrieval-research/
├── dataset/
│   ├── movies_clean.csv          ✅ 500 sinopsis film (subset TMDB)
│   └── queries.csv               ⏳ 30 kueri uji dan film targetnya (Tahap 3)
├── notebooks/
│   ├── 01_eda.ipynb              ✅ Exploratory Data Analysis
│   ├── 02_preprocessing.ipynb    ⏳ Uji tahapan preprocessing (Tahap 2)
│   ├── 03_tfidf_cosine.ipynb     ⏳ TF-IDF dan cosine similarity (Tahap 4)
│   └── 04_evaluasi.ipynb         ⏳ Hit Rate@5, MRR, dan analisis (Tahap 5-6)
├── src/
│   └── preprocess.py             ⏳ Fungsi pembersihan teks (Tahap 2)
├── models/
│   ├── tfidf_vectorizer.pkl      ⏳ Vectorizer skenario terbaik (Tahap 6)
│   └── tfidf_matrix.pkl          ⏳ Matriks dokumen skenario terbaik (Tahap 6)
├── results/
│   ├── fig_distribusi_panjang_sinopsis.png  ✅ Hasil EDA
│   ├── hasil_skenario.csv        ⏳ Metrik S1 sampai S4 (Tahap 5)
│   └── analisis_kegagalan.csv    ⏳ Penyebab kueri gagal (Tahap 6)
├── weekly_log.md                 ✅ Catatan progres per tahap
├── requirements.txt              ✅ Dependensi
├── .gitignore                    ✅
└── README.md                     ✅
```

## Cara Menjalankan

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

Buka notebook dari folder `notebooks/`. Notebook membaca data lewat path relatif `../dataset/movies_clean.csv`, jadi folder kerjanya harus `notebooks/`.

## Landasan Riset

1. **Holle dkk. (2026)**: membandingkan TF-IDF, Word2Vec, dan FastText dengan cosine similarity pada sinopsis film TMDb. TF-IDF memberi hasil terbaik dan tercepat. Dipakai sebagai pembenaran baseline dan acuan konfigurasi.
2. **Febrian & Permana (2026)**: sistem rekomendasi film berbasis konten (TF-IDF + cosine) pada sinopsis, dengan catatan kegagalan pada kata kunci ambigu. Dipakai sebagai contoh penerapan dan bahan analisis kegagalan.
3. **Alfian dkk. (2026)**: deteksi kemiripan judul pendek dengan TF-IDF + cosine, termasuk uji ablasi dengan dan tanpa stemming. Dipakai sebagai acuan rancangan perbandingan skenario preprocessing.

Daftar pustaka lengkap ditulis pada laporan akhir (Tahap 8).
