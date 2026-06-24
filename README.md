# 📊 Customer Retention Analytics 

### Nama : Ali Murthadho

### NIM : A11.2023.15269

---

## 📖 Deskripsi Proyek

Proyek ini merupakan implementasi Machine Learning untuk menganalisis perilaku pelanggan dan memprediksi kemungkinan pelanggan berhenti menggunakan layanan (Customer Churn).

Sistem dikembangkan sebagai tugas UAS Bengkel Koding Data Science dengan menerapkan tahapan Data Science mulai dari Data Understanding, Exploratory Data Analysis (EDA), Data Preprocessing, Model Training, Evaluasi Model, hingga Deployment menggunakan Streamlit.

---

## 🎯 Tujuan Proyek

* Menganalisis pola perilaku pelanggan berdasarkan data transaksi dan aktivitas.
* Mengidentifikasi faktor-faktor yang memengaruhi customer churn.
* Membangun model machine learning untuk memprediksi churn pelanggan.
* Membandingkan performa beberapa algoritma klasifikasi.
* Mengembangkan dashboard interaktif berbasis Streamlit.

---

## 📂 Dataset

Dataset yang digunakan berisi data aktivitas, transaksi, dan informasi pelanggan.

### Fitur Dataset

* Gender
* Age
* Country
* City
* Signup Date
* Last Purchase Date
* Acquisition Channel
* Device Type
* Subscription Type
* Is Premium User
* Total Visits
* Average Session Time
* Pages Per Session
* Email Open Rate
* Email Click Rate
* Total Spent
* Average Order Value
* Discount Used
* Support Tickets
* Refund Requested
* Delivery Delay Days
* Payment Method
* Satisfaction Score
* NPS Score
* Marketing Spend Per User
* Lifetime Value
* Last 3 Month Purchase Frequency

### Target

```text
Churn
```

Keterangan:

* 0 = Customer Bertahan
* 1 = Customer Churn

Jumlah Data:

```text
15.000 Data Pelanggan
```

---

## 🔍 Data Understanding

Tahapan analisis data yang dilakukan:

* Pemeriksaan struktur dataset
* Analisis tipe data
* Identifikasi missing values
* Pemeriksaan data duplikat
* Penentuan fitur dan target

---

## 🛠 Data Preprocessing

### 1. Missing Value Handling

* Mendeteksi data kosong
* Membersihkan data yang tidak lengkap

### 2. Duplicate Data Handling

* Pemeriksaan data duplikat
* Penghapusan data ganda

### 3. Encoding

Seluruh fitur kategorikal diubah menjadi numerik menggunakan Label Encoding.

### 4. Data Splitting

Dataset dibagi menjadi:

* Training Data (80%)
* Testing Data (20%)

---

## 📊 Exploratory Data Analysis (EDA)

Analisis yang dilakukan meliputi:

### Distribusi Data

* Age
* Total Visits
* Total Spent
* Average Session Time
* Lifetime Value

### Customer Churn Distribution

Visualisasi proporsi pelanggan churn dan non-churn.

### Correlation Analysis

Analisis hubungan antar fitur menggunakan heatmap korelasi.

### Outlier Analysis

Pendeteksian outlier menggunakan boxplot.

### Feature Relationship

Analisis hubungan antara fitur dan target churn.

---

## 🤖 Machine Learning Models

Model yang digunakan dalam penelitian:

### 1. Logistic Regression

Model klasifikasi linear untuk prediksi churn.

### 2. Random Forest

Model ensemble berbasis Decision Tree.

### 3. Voting Classifier

Kombinasi beberapa algoritma klasifikasi untuk meningkatkan performa prediksi.

---

## 🧪 Eksperimen Model

### Direct Modeling

Model dilatih langsung menggunakan data hasil preprocessing dasar.

### Enhanced Modeling

Model dilatih setelah dilakukan preprocessing tambahan.

### Hyperparameter Optimization

Optimasi parameter model menggunakan Grid Search untuk memperoleh performa terbaik.

---

## 📈 Total Model

```text
3 Algoritma × 3 Skenario = 9 Model
```

---

## 📏 Evaluasi Model

Model dievaluasi menggunakan:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

---

## 🏆 Best Model

```text
Random Forest Classifier
```

### Alasan Pemilihan

* Memiliki akurasi tinggi.
* Stabil pada data customer churn.
* Memberikan keseimbangan yang baik antara precision dan recall.
* Mampu menangani data kompleks dengan baik.

---

## 📌 Feature Importance

Fitur yang paling berpengaruh:

1. Total Spent
2. Satisfaction Score
3. Lifetime Value
4. Average Session Time
5. Support Tickets
6. Average Order Value
7. Pages Per Session

---

## 🚀 Deployment

Model terbaik disimpan menggunakan Joblib:

```python
joblib.dump(best_model, "best_model.pkl")
```

Aplikasi deployment dibangun menggunakan:

* Streamlit
* Scikit-Learn
* Pandas
* NumPy
* Joblib

---

## 🌐 Dashboard Features

Fitur yang tersedia pada aplikasi:

* Input data pelanggan secara interaktif.
* Prediksi churn secara real-time.
* Customer Risk Analysis.
* KPI Customer Summary.
* Dashboard sederhana dan responsif.

### Cara Menggunakan

1. Jalankan aplikasi Streamlit.
2. Masukkan data pelanggan.
3. Klik tombol **Analyze Customer**.
4. Sistem akan menampilkan hasil prediksi dan tingkat risiko churn.

---

## 📁 Struktur Project

```text
Projek-uas/
│
├── data/
│   └── customer_churn.csv
│
├── notebook/
│   └── Customer_Retention_Analytics.ipynb
│
├── deployment/
│   ├── app.py
│   └── best_model.pkl
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Instalasi

Clone repository:

```bash
git clone https://github.com/alimurthadho00/Projek-uas.git
cd Projek-uas
```

Install dependency:

```bash
pip install -r requirements.txt
```

---

## ▶️ Menjalankan Aplikasi

```bash
streamlit run deployment/app.py
```

atau

```bash
python -m streamlit run deployment/app.py
```

---

## 🔗 Repository GitHub

Repository proyek:

```text
https://github.com/alimurthadho00/Projek-uas
```

---

## 💻 Teknologi yang Digunakan

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib
* Streamlit

---

## 👨‍🎓 Author

**Ali Murthadho**

**NIM : A11.2023.15269**

Teknik Informatika

Universitas Dian Nuswantoro (UDINUS)

---

## 📄 License

Proyek ini dibuat untuk keperluan pembelajaran dan penyelesaian tugas UAS Bengkel Koding Data Science.
