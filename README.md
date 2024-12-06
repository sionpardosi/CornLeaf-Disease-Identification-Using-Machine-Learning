# **Identifikasi Jenis Penyakit Tanaman pada Daun Jagung Menggunakan Teknologi Machine Learning**

*Identification of Corn Leaf Diseases Using Machine Learning Technology*  

Proyek ini bertujuan untuk mengembangkan sistem deteksi penyakit tanaman jagung melalui **citra daun** menggunakan **Convolutional Neural Network (CNN)** dan **Transfer Learning DenseNet121**. Dengan pendekatan ini, petani dapat mendeteksi penyakit daun jagung secara otomatis dan cepat, meningkatkan efisiensi serta akurasi dalam diagnosis di lapangan.  

---

## **Deskripsi Proyek**

Tujuan utama proyek ini:  

1. Mengembangkan metode deteksi penyakit tanaman jagung berbasis citra.  
2. Menguji dan membandingkan akurasi model **CNN** dan **Transfer Learning DenseNet121**.  
3. Mengimplementasikan model dengan performa terbaik pada sistem deteksi penyakit berbasis gambar.  

Sistem ini dibangun menggunakan microframework **Flask** dengan bahasa pemrograman **Python**, memungkinkan integrasi dan pengujian model secara fleksibel.  

---

## **Pengumpulan Data**

Dataset diperoleh melalui survei dan observasi langsung di ladang jagung, menghasilkan:  

- **5,368 gambar** dan **10 video** daun jagung.  
- Data diklasifikasikan ke dalam 4 kelas:  
  - **Hawar Daun** (Blight)  
  - **Bercak Daun** (Leaf Spot)  
  - **Karat** (Rust)  
  - **Sehat** (Healthy)  

![Bukti Observasi](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Requirement/observasi%20-%20Copy.jpg)  

---

## **Fitur Utama**

- **Deteksi Penyakit Daun Jagung**: Mengidentifikasi penyakit seperti _Hawar Daun_, _Bercak Daun_, dan _Karat_.  
- **Pemrosesan Citra dengan OpenCV**: Melakukan augmentasi data untuk memperkaya dataset dan mencegah overfitting.  
- **Model Machine Learning**:  
  - **Convolutional Neural Network (CNN)**  
  - **Transfer Learning DenseNet121**  
- **Evaluasi Model**:  
  Menggunakan metrik seperti **precision**, **recall**, **F1-score**, dan **confusion matrix**.  
- **Visualisasi Data**: Menyediakan insight dari hasil analisis dataset.  

---

## **Preprocessing dan Augmentasi Gambar dengan Roboflow & OpenCV**

Untuk memastikan gambar berada dalam format yang sesuai dan meningkatkan akurasi model, kami menggunakan **Roboflow** & **OpenCV** untuk melakukan preprocessing dan augmentasi gambar secara otomatis. Berikut adalah teknik yang diterapkan:  

### **Preprocessing**

1. **Auto-Orient**: Menyesuaikan orientasi gambar agar tidak terbalik.  
2. **Static Crop**: Pemotongan gambar untuk memperkecil fokus:  
   - **Horizontal Region**: Pemotongan 25%-75% bagian horizontal.  
   - **Vertical Region**: Pemotongan 27%-75% bagian vertikal.  
3. **Resize**: Mengubah ukuran gambar menjadi **640x640 piksel**.  

### **Augmentasi**

1. **Outputs per Training Example**: Roboflow menghasilkan **3 output gambar** untuk setiap gambar dalam dataset.  
2. **Flip Horizontal**: Membalik gambar secara horizontal.  
3. **Grayscale**: 15% gambar diterapkan filter grayscale.  
4. **Hue**: Perubahan hue antara **-25° hingga +25°**.  
5. **Saturation**: Saturasi disesuaikan antara **-25% hingga +25%**.  
6. **Brightness**: Kecerahan gambar diubah dalam rentang **-25% hingga +25%**.  
7. **Exposure**: Exposure disesuaikan antara **-12% hingga +12%**.  
8. **Crop**: Gambar dipotong secara acak.  
9. **90 Derajat Rotation**: Gambar diputar 90 derajat.  

Dengan semua augmentasi ini, dataset menjadi lebih kaya dan model lebih tahan terhadap overfitting.  

---

## **Visualisasi Data**

Berikut adalah beberapa contoh visualisasi dari dataset:  

**Kelas Dataset**  
![Visualisasi Gambar Kelas Dataset](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Visualisasi%20gambar%20kelas%20dataset.png)  

**Canny Edge Detection**  
![Edge Detection](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Edge%20Detection.png)  

---

## **Evaluasi Model**

- **Confusion Matrix**:  
  Menunjukkan performa model dalam memprediksi setiap kelas.  
  ![Confusion Matrix](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Visualisasi%20Confusion%20Matrix.png)  

- **Overfitting Analysis**:  
  Membandingkan **Training Loss** dan **Validation Loss** untuk mendeteksi overfitting.  
  ![Validation Loss](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Visualisasi%20Performance%20Evaluasi%20Overfitting%20Validation%20Loss.png)  

---

## **Hasil**

- **Evaluasi**: Menilai hasil menggunakan metrik seperti **confusion matrix**, **precision**, **recall**, dan **F1-score**.  
- **Performance**: Model menunjukkan akurasi tinggi dalam mengidentifikasi penyakit daun jagung.  

---

## **Prediction**

### Prediction: Predict and Visualize a Single Image  
Melakukan prediksi terhadap satu gambar baru menggunakan model yang telah dilatih dan memvisualisasikan hasil prediksi dengan label kelasnya:  

![Visualisasi Prediction](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Visualisasi%20Data/Visualisasi%20Prediction.png)  

---

## **Kesimpulan**

Model **CNN** dan **DenseNet121** berhasil mendeteksi penyakit daun jagung dengan akurasi tinggi. Proyek ini menunjukkan potensi besar dalam implementasi AI untuk sektor pertanian, khususnya untuk diagnosis penyakit tanaman secara cepat dan efisien.  

---

## **Kontak**

Jika ada pertanyaan atau diskusi lebih lanjut, silakan hubungi:  
📧 **[spardosi12@gmail.com](mailto:spardosi12@gmail.com)**  

---

## **Lisensi**

Proyek ini dilisensikan di bawah [MIT License](LICENSE).  
