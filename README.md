# Identifikasi jenis penyakit tanaman pada daun jagung menggunakan teknologi machine learning - *Identification of corn leaf diseases using machine learning technology*

Proyek ini bertujuan untuk mengembangkan sistem deteksi penyakit tanaman jagung melalui **citra daun** menggunakan **Convolutional Neural Network (CNN)** dan **Support Vector Machine (SVM)**. Dengan pendekatan ini, petani dapat mendeteksi penyakit daun jagung secara otomatis dan cepat, yang akan meningkatkan efisiensi serta akurasi dalam diagnosis penyakit daun jagung di lapangan.

### Deskripsi Proyek
Penelitian ini bertujuan untuk:
1. Mengembangkan metode deteksi penyakit tanaman jagung melalui citra daun.
2. Menguji dan membandingkan akurasi model **CNN** dan **SVM**.
3. Mengimplementasikan model dengan akurasi tertinggi pada sistem deteksi penyakit berbasis citra.

Sistem ini dibangun menggunakan microframework **Flask** dengan bahasa pemrograman **Python** untuk memungkinkan integrasi dan pengujian model deteksi penyakit secara fleksibel.

### Pengumpulan Data
Dataset pada penelitian ini diperoleh melalui survei langsung dan observasi di ladang jagung masyarakat, menghasilkan:
- **500 gambar** dan **10 video** daun jagung.
- Data tersebut diklasifikasikan ke dalam 4 kelas: **Hawar**, **bercak daun**, **Karat**, dan **Sehat**.
  
### **Bukti Observasi Langsung**
![Bukti Observasi](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Requirement/observasi%20-%20Copy.jpg)

### Fitur Utama

- **Deteksi Penyakit Daun Jagung**: Mengidentifikasi penyakit seperti _Bercak Daun_ (Leaf Spot), _Karat Jagung_ (Rust), dan _Hawar Daun_ (Blight).
- **Pemrosesan Citra**: Augmentasi gambar untuk memperkaya dataset dan menghindari overfitting, termasuk proses **rescale**, **rotate**, **zoom**, dan **flip**.
- **Model Machine Learning**: Algoritma **CNN** dan **SVM** diterapkan untuk klasifikasi gambar.
- **Evaluasi Model**: Pengukuran akurasi menggunakan **precision**, **recall**, **F1-score**, dan **confusion matrix** untuk hasil yang optimal.

### Teknologi yang Digunakan

- **Confusion matrix** digunakan untuk mengukur akurasi model, dan pengujian dilakukan menggunakan **Jupyter Notebook** / **Google Colab** dan **Visual Studio Code** sebagai teks editor utama.
- **Python**: Bahasa pemrograman utama untuk pengembangan model.
- **TensorFlow** atau **PyTorch**: Framework untuk membangun model CNN.
- **OpenCV**: Digunakan untuk pemrosesan citra dan augmentasi gambar.
- **Matplotlib**: Untuk visualisasi hasil dan evaluasi model.

---

### Hasil (Coming Soon)

- **Preprocessing**: Tahapan ini mengolah citra untuk mempermudah algoritma CNN dan SVM dalam proses training, dengan menggunakan augmentasi data seperti rescale, rotate, zoom, dan flip.
- **Pelatihan**: Data latih digunakan untuk mengajari model mengenali ciri-ciri dari setiap jenis penyakit melalui proses iteratif.
- **Pengujian**: Model yang telah dilatih diuji dengan dataset uji untuk mengukur akurasi dan performanya dalam mendeteksi penyakit.
- **Evaluasi** -> Coming Soon
  
---

Dengan adanya sistem ini, diharapkan proses diagnosis penyakit tanaman jagung dapat dilakukan lebih cepat dan efisien.
