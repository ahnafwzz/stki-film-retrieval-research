# Weekly Log Progres Tugas Akhir STKI

Catatan progres proyek CineMatch per tahap. Setiap tahap diberi tanggal dan dikerjakan dengan commit tersendiri di repositori ini.

## Ringkasan Tahap

| Tahap | Kegiatan | Tanggal | Status |
|-------|----------|---------|--------|
| 1 | Inisiasi proyek, dataset, dan EDA | 26 Okt 2026 | Selesai ✅ |
| 2 | Modul `preprocess.py` (S1 sampai S4) | - | Belum |
| 3 | Pemilihan 30 film target dan penulisan 30 kueri uji | - | Belum |
| 4 | TF-IDF, cosine similarity, dan fungsi ranking | - | Belum |
| 5 | Eksperimen S1 sampai S4 (Hit Rate@5 dan MRR) | - | Belum |
| 6 | Analisis kegagalan dan ekspor model | - | Belum |
| 7 | Aplikasi Streamlit (repo produk) | - | Belum |
| 8 | Laporan akhir dan persiapan demo | - | Belum |

---

## Tahap 1: Inisiasi Proyek & Eksplorasi Data (EDA)

**Tanggal:** 26 Oktober 2026
**Target:** Menyiapkan dataset bersih, membuat struktur repositori, melakukan EDA, dan mencatat pustaka landasan.
**Status:** Selesai ✅

### Rincian Pekerjaan

1. **Pemotongan dataset.** Mengunduh *TMDB 5000 Movie Dataset* dari Kaggle, mengambil kolom `title` dan `overview`, lalu memotongnya menjadi 500 baris pertama sesuai urutan asli file (bukan sampel acak) untuk menekan beban komputasi. Hasilnya disimpan sebagai `dataset/movies_clean.csv`.
2. **Penyiapan repositori.** Membuat struktur folder, `README.md`, `requirements.txt` (pandas, matplotlib, scikit-learn, nltk, dan pendukung notebook), serta `.gitignore`.
3. **EDA.** Notebook `notebooks/01_eda.ipynb` memeriksa kelengkapan data, duplikasi, panjang sinopsis, karakter khusus, kata paling sering, dan ukuran kosakata awal. Histogram panjang sinopsis disimpan di `results/fig_distribusi_panjang_sinopsis.png`.
4. **Studi pustaka.** Menetapkan tiga jurnal landasan beserta poin yang akan dikutip di laporan akhir:

   | Jurnal | Poin yang dikutip |
   |--------|-------------------|
   | **Holle dkk. (2026)**, MALCOM 6(3) | TF-IDF + cosine terbaik dan tercepat dibanding Word2Vec dan FastText pada sinopsis film TMDb (Tabel 4, hal. 1650: P@10 0,835 vs 0,780 vs 0,740). Konfigurasi TF-IDF dengan `min_df=1` dan normalisasi L2 (bagian 2.3, hal. 1644). Keterbatasan: relevansi berbasis genre dan belum ada uji signifikansi (hal. 1653). |
   | **Febrian & Permana (2026)**, Al-Aqlu 4(1) | Rekomendasi film berbasis konten (TF-IDF + cosine) pada sinopsis, dengan Precision@5 30% (Gambar 1, hal. 22). Kegagalan pada kata kunci ambigu, misalnya pencarian "Hulk" yang cocok dengan film lain yang memuat nama "Bruce" (hal. 22-23). |
   | **Alfian dkk. (2026)**, JITEKH 14(2) | Acuan rancangan uji ablasi dengan vs tanpa stemming (bagian 3.8, hal. 152-153) dan temuan bahwa model leksikal gagal pada sinonim (bagian 3.7, hal. 152). Catatan: angka akurasi pada abstrak tidak konsisten dengan Tabel 2-3 dan Gambar 5, sehingga jurnal ini hanya dipakai sebagai acuan desain, bukan acuan angka. |

### Temuan Penting

- Dataset berisi 500 film, 2 kolom, tanpa missing value, dan tanpa baris, judul, maupun sinopsis duplikat.
- Panjang sinopsis rata-rata 54,9 kata (median 51,5), terpendek 12 kata dan terpanjang 174 kata. Ada 14 sinopsis di bawah 20 kata.
- Pada teks mentah, 20 kata teratas semuanya kata fungsi atau sisa apostrof `s`, dengan porsi 32,1% dari 27.990 token. Ini mendukung pengujian stopword removal (S3).
- Kosakata unik: 8.181 (dipisah spasi saja) dan 6.011 (huruf kecil, hanya huruf). Angka ini menjadi pembanding awal untuk S1 dan S2.
- Apostrof lengkung (’) ada di 28 sinopsis, apostrof lurus (') di 214, angka di 103, dan karakter non-ASCII di 81. Semuanya harus ditangani di `preprocess.py`.

### Catatan dan Keterbatasan

- Subset 500 baris pertama bukan sampel acak, sehingga hasil eksperimen tidak digeneralisasi ke seluruh dataset TMDB.
- Sinopsis yang pendek membatasi informasi yang bisa dicocokkan dan dicatat sebagai salah satu kategori penyebab kegagalan pada analisis di Tahap 6.

### Rencana Tahap 2

- Membuat `src/preprocess.py` dengan fungsi untuk skenario S1 sampai S4 (case folding, hapus tanda baca dan angka, stopword removal, stemming Porter).
- Menangani apostrof tanpa menyisakan token satu huruf.
- Mendokumentasikan uji coba pada beberapa sinopsis di `notebooks/02_preprocessing.ipynb`.
