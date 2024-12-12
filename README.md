# 🌽 Identifikasi Jenis Penyakit Tanaman pada Daun Jagung Menggunakan Teknologi Machine Learning

_Identification of Corn Leaf Diseases Using Machine Learning Technology_

Proyek ini bertujuan untuk mengembangkan sistem deteksi penyakit tanaman jagung melalui **citra daun** menggunakan **Convolutional Neural Network (CNN)** dan **Model Transfer Learning DenseNet121**. Dengan pendekatan ini, petani dapat:

- Mendeteksi penyakit daun jagung secara otomatis dan cepat.
- Meningkatkan efisiensi serta akurasi dalam diagnosis penyakit di lapangan.

---

# **Visualisasi Prediksi Sistem**

> Berikut adalah hasil prediksi dari sistem yang telah dikembangkan. Sistem ini mampu mengidentifikasi penyakit daun jagung dengan akurasi tinggi, memberikan diagnosa cepat secara real-time.

<div align="center">
  <a href="https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/videopredict-ezgif.com-video-to-gif-converter.gif">
    <img src="https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/videopredict-ezgif.com-video-to-gif-converter.gif" alt="Video Prediksi" width="70%" style="border: 2px solid #4CAF50; border-radius: 8px;">
  </a>
</div>

---

# **Deskripsi Proyek**

Penelitian ini bertujuan untuk:

1. 🌱 **Mengembangkan metode deteksi penyakit tanaman jagung** melalui citra daun menggunakan **Jupyter Notebook (IPython Notebook)** sebagai platform pemrosesan data dan pengembangan model.
2. 🔍 **Menguji dan membandingkan akurasi** model **Convolutional Neural Network (CNN)** dan **Transfer Learning DenseNet121** untuk mendapatkan kinerja terbaik.
3. 🚀 **Mengimplementasikan model terbaik** pada sistem deteksi penyakit berbasis citra menggunakan teknologi machine learning.

Sistem ini dirancang untuk memprediksi penyakit melalui antarmuka web yang dibangun menggunakan **Flask**, sebuah microframework berbasis Python. Pendekatan ini memungkinkan integrasi yang mulus dan pengujian model secara fleksibel serta efisien.

---

# **Pengumpulan Data**

Dataset pada penelitian ini diperoleh melalui survei langsung dan observasi di ladang jagung masyarakat, menghasilkan:

- 🖼️ **5,368 gambar** dan 🎥 **10 video** daun jagung.
- Data diklasifikasikan ke dalam 4 kelas:
  - 🍂 **Hawar Daun** (_Blight_).
  - 🍃 **Bercak Daun** (_Leaf Spot_).
  - 🌾 **Karat** (_Rust_).
  - 🌿 **Sehat** (_Healthy_).

---

### 📸 **Bukti Observasi Langsung**

<div align="center">
  <img src="https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Requirement/observasi%20-%20Copy.jpg" 
       alt="Bukti Observasi" 
       width="70%" 
       style="border: 2px solid #4CAF50; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
  <p style="font-style: italic; color: #555;">*Gambar hasil survei langsung di ladang jagung masyarakat*</p>
</div>

---

# 🌟 **Fitur Utama**

- 🔎 **Deteksi Penyakit Daun Jagung**:  
  Identifikasi penyakit seperti _Hawar Daun_, _Bercak Daun_, dan _Karat_.
- 🖼️ **Pemrosesan Citra**:  
  Melakukan augmentasi data untuk memperkaya dataset dan mencegah overfitting.
- 🤖 **Model Machine Learning**:
  - **Convolutional Neural Network (CNN)**
  - **Transfer Learning DenseNet121**
- 🎛️ **Hyperparameter Tuning**:  
  Menyesuaikan parameter untuk optimasi kinerja model.
- 📈 **Evaluasi Model**:  
  Menggunakan metrik seperti **precision**, **recall**, **F1-score**, dan **confusion matrix**.
- 📊 **Visualisasi Kinerja Model**:  
  Menyediakan insight dari hasil analisis dataset.
- 🎯 **Prediksi Akurat**:  
  Melakukan prediksi terhadap gambar uji dengan model yang telah dilatih.

---

# Teknologi yang Digunakan

#### **Tools:**

<p>
    <img src="https://img.shields.io/badge/Language-Python-blue?logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Framework-Flask-green?logo=flask&logoColor=white" />
    <img src="https://img.shields.io/badge/Algorithm-CNN-orange?logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Algorithm-SVM-blue?logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Library-TensorFlow-red?logo=tensorflow&logoColor=white" />
    <img src="https://img.shields.io/badge/Library-OpenCV-lightblue?logo=opencv&logoColor=white" />
    <img src="https://img.shields.io/badge/Library-Matplotlib-005C4B?logo=matplotlib&logoColor=white" />
    <img src="https://img.shields.io/badge/Tool-Jupyter%20Notebook-FFD43B?logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Tool-Google%20Colab-FF6F00?logo=googlecolab&logoColor=white" />
    <img src="https://img.shields.io/badge/Editor-Visual%20Studio%20Code-007ACC?logo=visualstudiocode&logoColor=white" />
</p>

---

# **Preprocessing dan Augmentasi Gambar dengan Roboflow & OpenCV**

Untuk memastikan gambar dalam format yang sesuai dan meningkatkan akurasi model, kami menggunakan **Roboflow** dan **OpenCV** untuk melakukan preprocessing serta augmentasi gambar secara otomatis. Berikut adalah teknik yang diterapkan:

---

## **Preprocessing**

Proses preprocessing bertujuan untuk menyiapkan gambar dengan format yang optimal. Teknik yang digunakan meliputi:

1. **Auto-Orient**  
   Menyesuaikan orientasi gambar agar tidak terbalik.

2. **Static Crop**  
   Memotong gambar untuk memperkecil fokus:

   - **Horizontal Region**: Memotong 25%-75% bagian horizontal.
   - **Vertical Region**: Memotong 27%-75% bagian vertikal.

3. **Resize**  
   Mengubah ukuran gambar menjadi **640x640 piksel** agar konsisten dengan input model.

---

## **Augmentasi**

Augmentasi digunakan untuk memperkaya variasi dataset dan mengurangi risiko overfitting. Teknik yang diterapkan meliputi:

<div style="max-height: 300px; overflow-y: scroll; padding-right: 10px;">
1. **Outputs per Training Example**  
   - Menghasilkan **3 output gambar** untuk setiap gambar dalam dataset.

2. **Flip Horizontal**  
   - Membalik gambar secara horizontal untuk menambah variasi orientasi.

3. **Grayscale**  
   - Menerapkan filter grayscale pada **15% gambar** untuk menangkap pola warna yang netral.

4. **Hue**  
   - Menyesuaikan hue dalam rentang **-25° hingga +25°**.

5. **Saturation**  
   - Mengubah saturasi warna dalam rentang **-25% hingga +25%**.

6. **Brightness**  
   - Menyesuaikan kecerahan gambar dalam rentang **-25% hingga +25%**.

7. **Exposure**  
   - Mengatur exposure dalam rentang **-12% hingga +12%**.

8. **Crop**  
   - Melakukan pemotongan acak untuk menghasilkan variasi gambar.

9. **Rotasi 90 Derajat**  
   - Memutar gambar sebesar **90°** untuk meningkatkan orientasi data.

10. **Histogram Equalization & Median Filtering**  
    - Teknik ini digunakan untuk meningkatkan kualitas visual gambar.
</div>

### **Manfaat Teknik Ini**

Dengan preprocessing dan augmentasi yang cermat:

- Dataset menjadi lebih **kaya** dan **beragam**.
- Model menjadi lebih **tahan terhadap overfitting** dan memiliki **generalizability** yang lebih baik.
- Variasi gambar membantu model mengenali pola dari berbagai kondisi cahaya, warna, dan orientasi.

---

## **Visualisasi Data Gambar**

Tahap visualisasi dilakukan untuk memberikan gambaran mengenai kelas-kelas yang ada dalam dataset. Hal ini bertujuan untuk memastikan distribusi data yang seimbang dan memahami karakteristik visual dari setiap kelas. Berikut adalah contoh gambar dari dataset:

![Visualisasi Gambar Kelas Dataset](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Visualisasi%20gambar%20kelas%20dataset.png)

---

## **Penerapan Canny Edge Detection**

Pada tahap ini, kami menerapkan **Canny Edge Detection** untuk memvisualisasikan tepi (edges) pada gambar daun jagung. Teknik ini membantu mengidentifikasi fitur penting pada gambar, sehingga model dapat lebih fokus pada elemen yang relevan untuk klasifikasi.

Contoh hasil Canny Edge Detection:

![Visualisasi Edge Detection](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Edge%20Detection.png)

### **Keunggulan Teknik Visualisasi**

1. **Visualisasi Gambar Dataset**:

   - Memberikan pemahaman mendalam tentang karakteristik visual dari setiap kelas.
   - Membantu dalam proses analisis awal dan validasi dataset.

2. **Canny Edge Detection**:
   - Membantu model dalam mengenali pola tepi yang signifikan pada gambar.
   - Meminimalkan gangguan dari fitur yang tidak relevan.

Dengan teknik visualisasi ini, proses pelatihan model menjadi lebih efisien karena fokus pada elemen penting yang mendukung akurasi klasifikasi.

---

# Class Distribution

class_labels = {0: 'Bercak', 1: 'Hawar', 2: 'Karat', 3: 'Sehat'}

![Class Distribution Dataset](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Class%20Distribution%20Dataset.png)

---

# **Arsitektur Model CNN Kustom**

_Identifikasi Jenis Penyakit Tanaman pada Daun Jagung_

Arsitektur model CNN kustom dirancang untuk mengenali pola unik pada citra daun jagung, seperti tekstur, warna, dan tepi. Model ini dirancang khusus untuk kasus identifikasi penyakit pada daun jagung, dengan lapisan konvolusi dan pooling yang dioptimalkan untuk performa tinggi.

<p align="center">
  <img src="https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Aksitektur%20model.png" alt="Arsitektur Model CNN Kustom" width="80%">
</p>

---

# **Arsitektur Model Transfer Learning DenseNet121**

_Identifikasi Jenis Penyakit Tanaman pada Daun Jagung_

Model **DenseNet121** menggunakan pendekatan transfer learning, memanfaatkan bobot awal yang telah dilatih pada dataset besar untuk meningkatkan akurasi dan efisiensi pelatihan. Arsitektur ini memungkinkan pendeteksian pola kompleks dengan lapisan dense yang saling terhubung.

<p align="center">
  <img src="https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Aksitektur%20model%20denseNet121.png" alt="Arsitektur Model Transfer Learning DenseNet121" width="80%">
  <p style="font-style: italic; color: #555;">*Visualisasi lengkap arsitektur model DenseNet121 dapat ditemukan dalam kode pada file app.ipynb.*</p>
</p>

---

# Evaluasi Model

Model dievaluasi dengan data validasi untuk mengukur _loss_ dan _accuracy_. Ini memberikan gambaran tentang kinerja model pada data yang tidak terlihat sebelumnya:

### **Evaluasi Model CNN-Costum pada Data Validasi (Visualisasi Validation Accuracy)**:

![Visualisasi Validation Accuracy](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Visualisasi%20Validation%20Accuracy.png)

### **Evaluasi Model Transfer Learning DenseNet121 pada Data Validasi (Visualisasi Validation Accuracy)**:

![Visualisasi Validation Accuracy](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Visualisasi%20Validation%20Accuracy%20denseNet121.png)

---

### **Evaluasi dengan Confusion Matrix**:

Confusion Matrix digunakan untuk mengukur prediksi model vs label sebenarnya, memberikan wawasan lebih mendalam tentang kesalahan klasifikasi.
-> Menghitung **Confusion Matrix** untuk menilai distribusi prediksi, Menampilkan **Classification Report** yang mencakup Precision, Recall, dan F1-Score, Menampilkan hasil precision, recall, dan f1-score.

#### **Rumus Masing Masing Parameter**:

![Rumus](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Rumus%20Confusion%20Matrix.png)

#### **Rumus Tabel Confusion Matrix**:

![Rumus](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Rumus%20Tabel%20Confusion%20Matrix.png)

### **Visualisasi Confusion Matrix Model CNN-Costum**:

![Visualisasi Confusion Matrix](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Visualisasi%20Confusion%20Matrix.png)

### **Visualisasi Confusion Matrix Model Transfer Learning DenseNet121**:

![Visualisasi Confusion Matrix](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Visualisasi%20Confusion%20Matrix%20denseNet121.png)

---

### **Classification Report Model CNN-Costum**:

![Hasilnya](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Classification%20Report.png)

### **Classification Report Model Tranfer Learning DenseNet121**:

![Hasilnya](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Classification%20Report%20denseNet121.png)

---

# Perfomance

1. **Plot Loss**: Menampilkan perbandingan antara **Training Loss** dan **Validation Loss**.
2. **Plot Akurasi**: Menampilkan perbandingan antara **Training Accuracy** dan **Validation Accuracy**.
3. **Interpretasi**: Mengamati apakah ada perbedaan signifikan antara akurasi pelatihan dan validasi yang menunjukkan **overfitting** atau **underfitting**.

### Performance: Evaluasi Overfitting Model CNN-Costum

![Visualisasi Performance Evaluasi Overfitting Validation Loss](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Visualisasi%20Performance%20Evaluasi%20Overfitting%20Validation%20Loss.png)

![Visualisasi Performance Evaluasi Overfitting Validation Accuracy](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Visualisasi%20Performance%20Evaluasi%20Overfitting%20Validation%20Accuracy.png)

### Performance: Evaluasi Overfitting Model Transfer Learning DenseNet121

![Visualisasi Performance Evaluasi Overfitting Validation Accuracy](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Visualisasi%20Performance%20Accuracy%20dan%20loss%20training%20dan%20validation%20DenseNet121.jpg)

---

# **Hasil dan Pembahasan**

Algoritma CNN-Kostum berhasil mencapai akurasi 98% dengan loss 0,16, menunjukkan kemampuan mempelajari pola secara optimal tanpa overfitting. Sebagai pembanding, DenseNet121 mencapai akurasi 97,7% dengan waktu pelatihan lebih lama, mengindikasikan keunggulan dalam jaringan yang lebih kompleks.

Tuning hyperparameter, termasuk learning rate 0,0001, batch size 32, dan 50 epoch, memberikan kontribusi signifikan terhadap peningkatan performa model. Dataset diproses melalui normalisasi, resize, dan augmentasi, yang efektif meningkatkan generalisasi model terhadap variasi data. Pembagian data menjadi 80% latih dan 20% uji memastikan evaluasi yang adil dan bebas bias.

Hasil menunjukkan bahwa kombinasi preprocessing, arsitektur CNN-Kostum, dan optimisasi hyperparameter mampu memberikan performa optimal. Meski DenseNet121 menawarkan akurasi lebih tinggi, CNN-Kostum unggul dalam efisiensi waktu pelatihan, menjadikannya solusi praktis untuk implementasi dalam teknologi pertanian.

---

# Prediction

### Prediction: Predict and Visualize a Single Image

Melakukan prediksi terhadap satu gambar baru menggunakan model yang telah dilatih dan visualisasikan hasil prediksi dengan label kelasnya:

![Visualisasi Prediction](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Visual%20Prediction.png)

---

# Kesimpulan

Model CNN dan **DenseNet121** telah menunjukkan potensi yang sangat baik dalam mendeteksi penyakit daun jagung dengan tingkat akurasi yang memadai. Penelitian ini membuka jalan untuk pengembangan sistem deteksi otomatis berbasis AI dalam pertanian untuk mempermudah dan mempercepat diagnosis penyakit tanaman jagung.

---

# Langkah-Langkah Menjalankan Proyek

## 1. Download atau Clone Repository

- Buka terminal atau command prompt.
- Clone repository dengan perintah:
  ```bash
  git clone https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning.git
  ```

Atau, unduh proyek dalam format ZIP melalui tombol "Code" di halaman GitHub dan ekstrak file ke direktori yang diinginkan.

## 2. Instalasi Dependensi

- Masuk ke direktori proyek:
  ```bash
  cd CornLeaf-Disease-Identification-Using-Machine-Learning
  ```

## 3. Persiapkan Dataset

Unduh dataset yang diperlukan dengan menggunakan Roboflow dari folder Dataset/ : [tautan GitHub](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Dataset/Dataset.txt).

## 4. Menjalankan Model

⚠️ **Ingat!!!**  
Model yang dilatih sudah disimpan, sehingga **tidak perlu melakukan pelatihan data lagi**. Anda dapat mencoba memakai model berikut:

- **Model_CNN_256px.keras**
- **Model_CNN_128px.keras**
- **Model_denseNet121_256px.keras**
- **Model_denseNet121_128px.keras**

Pastikan Anda memiliki salah satu dari platform berikut untuk menjalankan model:

- **Jupyter Notebook**: Jalankan file `.ipynb` langsung di Jupyter Notebook.
- **Google Colab**: Jika Anda lebih suka menggunakan Google Colab, Anda dapat mengunggah file `.ipynb` ke Google Colab dan menjalankannya di sana.
- **Visual Studio Code (VS Code)**: Pastikan Anda telah menginstal Visual Studio Code dan menambahkan Jupyter Extension. Untuk menjalankan notebook `.ipynb` di VS Code, pastikan Anda memiliki virtual environment dengan `ipykernel` yang terinstal.

### Menjalankan model dan pelatihan melalui Kode .ipynb :

0. **Buka Kode app.ipynb**

1. **Import Libraries and Modules**:
   Pastikan untuk menjalankan import semua libraries dan modul yang diperlukan di dalam kode.

2. **Jalankan Arsitektur Model CNN**:
   Lakukan inisialisasi dan definisi arsitektur model CNN seperti yang ada dalam kode.

3. **Jalankan Load Model yang Sudah Disimpan**:
   Karena epoch model sudah disimpan, gunakan kode berikut untuk memuat model yang telah disimpan di folder sehingga tidak perlu melakukan pelatihan (Epoch) ulang :
   `model/model2.keras` dan `model2.h5`

4. **Lakukan Percobaan Accuracy**:
   Setelah model dimuat, jalankan perintah kode yang sudah ada untuk menguji akurasi model dengan dataset yang ada.

5. **Uji Evaluasi dan Performance**:
   Jalankan kode uji untuk melihat hasil evaluasi dan performa model menggunakan dataset pengujian.

6. **Prediksi Gambar**:
   Untuk melihat hasil prediksi pada gambar tertentu, sesuaikan path gambar yang ingin Anda prediksi:
   `img_path = 'Testing/test.jpg'  # Ganti dengan path gambar`

### Jika ingin menjalankan server aplikasi Flask untuk testing dan prediksi, gunakan perintah:

`python app.py`

## 5. Akses Aplikasi Web

Setelah aplikasi Flask berjalan, buka browser dan akses:
http://127.0.0.1:5000/

Aplikasi ini akan memungkinkan Anda untuk mengupload gambar daun jagung dan melihat hasil prediksi jenis penyakit.

# License

This project is licensed under the [MIT License](LICENSE).
