# UTS Pemrograman IoT IFB309 - Yosua Aronggear

## 🧍 Identitas
- **Nama:** Yosua Aronggear  
- **NRP:** 152023019  
- **Kelas:** BB  
- **Mata Kuliah:** Pemrograman IoT (IFB309)  
- **Semester:** Genap 2025/2026  

---

## 📘 Deskripsi Proyek
Proyek ini merupakan implementasi dari **UTS Pemrograman IoT IFB309**.  
Saya membuat aplikasi **backend menggunakan Flask** yang menghasilkan data sensor secara acak dalam format **JSON**.  

Data sensor yang dihasilkan terdiri dari:
- Suhu (°C)  
- Kelembapan (%)  
- Intensitas Cahaya (Lux)  
- Timestamp (Waktu Pengambilan Data)  

Selain backend, saya juga membuat aplikasi **parser.py** yang berfungsi untuk mengambil data JSON dari server Flask dan menampilkan hasil parsing ke terminal.

---

## ⚙️ Cara Menjalankan Program

### 1️⃣ Instalasi Library
Pastikan Python sudah terinstal di komputer.  
Lalu jalankan perintah berikut di terminal untuk menginstal semua library yang dibutuhkan:
```bash
pip install -r requirements.txt
```

### 2️⃣ Jalankan Backend Flask
```bash
python app.py
```

Jika berhasil, terminal akan menampilkan pesan:
```
🌐 Server berjalan di http://127.0.0.1:5000
```

### 3️⃣ Akses Data JSON di Browser
Buka browser dan ketik:
```
http://127.0.0.1:5000/data
```
Data JSON hasil dari backend Flask akan muncul di halaman browser.

### 4️⃣ Jalankan Parsing JSON
Buka terminal baru (jangan hentikan Flask), lalu jalankan:
```bash
python parser.py
```
Program akan menampilkan:
- Data mentah dalam format JSON  
- Hasil parsing data terakhir (suhu, kelembapan, lux, dan timestamp)

---

## 🧪 Hasil Program
Berikut hasil dari masing-masing bagian tugas UTS:

1. **Nomor 1b - Backend Flask**  
   Backend berhasil menampilkan data sensor dalam format JSON pada browser.

2. **Nomor 2a - JSON Editor Online**  
   Data JSON dari backend berhasil ditampilkan di situs [jsoneditoronline.org](https://jsoneditoronline.org)  
   dalam tampilan **Tree View** untuk memperlihatkan struktur data yang jelas.

3. **Nomor 2b - Parsing JSON**  
   Aplikasi parser berhasil mengambil data JSON dari server Flask  
   dan menampilkan hasil parsing data sensor di terminal.

---

## 📎 File yang Digunakan
- `app.py` → Backend Flask untuk menghasilkan data JSON  
- `parser.py` → Mengambil dan mem-parsing data JSON  
- `requirements.txt` → Daftar library yang diperlukan  
- `README.md` → Dokumentasi proyek  

---

## 🧾 Dokumentasi Pendukung
- **File PDF Jawaban:** `UTS_IFB309_2526_BB_152023019_Yosua_Aronggear.pdf`  
- **Video Demonstrasi:** `UTS_IFB309_2526_BB_152023019_Yosua_Aronggear.mp4`

---

## 👨‍💻 Pembuat
> **Nama:** Yosua Aronggear  
> **NRP:** 152023019  
> **Kelas:** BB  
> **Institut Teknologi Nasional**  
> **Mata Kuliah:** Pemrograman IoT (IFB309)  
> **Tahun Ajaran:** 2025/2026
