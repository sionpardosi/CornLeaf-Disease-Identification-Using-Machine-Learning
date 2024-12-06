# Identifikasi Jenis Penyakit Tanaman pada Daun Jagung Menggunakan Teknologi Machine Learning

*Identification of corn leaf diseases using machine learning technology* 

Proyek ini bertujuan untuk mengembangkan sistem deteksi penyakit tanaman jagung melalui **citra daun** menggunakan **Convolutional Neural Network (CNN)** dan **Model Transfer Learning DenseNet121**. Dengan pendekatan ini, petani dapat mendeteksi penyakit daun jagung secara otomatis dan cepat, yang akan meningkatkan efisiensi serta akurasi dalam diagnosis penyakit daun jagung di lapangan.

### Deskripsi Proyek
Penelitian ini bertujuan untuk:
1. Mengembangkan metode deteksi penyakit tanaman jagung melalui citra daun.
2. Menguji dan membandingkan akurasi model **CNN** dan **Model Transfer Learning DenseNet121**.
3. Mengimplementasikan model dengan akurasi tertinggi pada sistem deteksi penyakit berbasis citra.

Sistem ini dibangun menggunakan microframework **Flask** dengan bahasa pemrograman **Python** untuk memungkinkan integrasi dan pengujian model deteksi penyakit secara fleksibel.

### Pengumpulan Data
Dataset pada penelitian ini diperoleh melalui survei langsung dan observasi di ladang jagung masyarakat, menghasilkan:
- **5368 gambar** dan **10 video** daun jagung.
- Data tersebut diklasifikasikan ke dalam 4 kelas: **Hawar**, **bercak daun**, **Karat**, dan **Sehat**.
  
### **Bukti Observasi Langsung**
![Bukti Observasi](https://github.com/sionpardosi/CornLeaf-Disease-Identification-Using-Machine-Learning/blob/main/Requirement/observasi%20-%20Copy.jpg)

### Fitur Utama

- **Deteksi Penyakit Daun Jagung**: Mengidentifikasi penyakit seperti _Bercak Daun_ (Leaf Spot), _Karat Jagung_ (Rust), dan _Hawar Daun_ (Blight).
- **Pemrosesan Citra - Roboflow / OpenCV**: Augmentasi gambar untuk memperkaya dataset dan menghindari overfitting, termasuk proses **rescale**, **rotate**, **zoom**, dan **flip**.
- **Model Machine Learning**: Algoritma **CNN** dan **Transfer Learning DenseNet121** diterapkan untuk klasifikasi gambar.
- **Evaluasi Model**: Pengukuran akurasi menggunakan **precision**, **recall**, **F1-score**, dan **confusion matrix** untuk hasil yang optimal.

### Preprocessing dan Augmentasi Gambar dengan Roboflow

Dalam proyek ini, kami menggunakan **Roboflow** untuk melakukan preprocessing dan augmentasi gambar secara otomatis. Berikut adalah langkah-langkah yang diterapkan untuk mempersiapkan gambar sebelum digunakan dalam pelatihan model.

#### Preprocessing

Preprocessing adalah tahap penting yang dilakukan untuk memastikan gambar berada dalam format dan ukuran yang sesuai dengan kebutuhan model. Berikut adalah beberapa teknik preprocessing yang diterapkan:

1. **Auto-Orient:** Menyesuaikan orientasi gambar untuk memastikan gambar dalam posisi yang benar dan tidak terbalik.
2. **Static Crop:** Gambar dipotong pada area tertentu untuk memperkecil fokus:
   - **Horizontal Region:** Pemotongan dilakukan pada **25%-75%** bagian horizontal gambar.
   - **Vertical Region:** Pemotongan dilakukan pada **27%-75%** bagian vertikal gambar.
3. **Resize:** Gambar akan diubah ukurannya menjadi **640x640** piksel untuk memastikan ukuran input yang konsisten pada model.

#### Augmentasi

Untuk memperkaya dataset dan meningkatkan akurasi model, augmentasi gambar digunakan. Dengan Roboflow, kami dapat melakukan berbagai augmentasi secara otomatis, seperti:

1. **Outputs per Training Example:** Untuk setiap gambar dalam dataset, Roboflow menghasilkan **3 output gambar** yang berbeda untuk meningkatkan variasi dalam data pelatihan.
2. **Flip Horizontal:** Melakukan flip gambar secara horizontal (spion kiri-kanan) untuk menciptakan variasi dalam orientasi objek.
3. **Grayscale:** 15% dari gambar diterapkan dengan filter grayscale untuk menambah variasi dalam warna gambar.
4. **Hue:** Perubahan hue gambar dilakukan dalam rentang **-25° hingga +25°** untuk variasi warna.
5. **Saturation:** Saturasi gambar disesuaikan antara **-25% hingga +25%** untuk variasi kecerahan warna.
6. **Brightness:** Kecerahan gambar diubah dalam rentang **-25% hingga +25%**.
7. **Exposure:** Exposure gambar disesuaikan antara **-12% hingga +12%** untuk perubahan kontras.
8. **Crop:** Gambar akan dipotong secara acak untuk meningkatkan variasi objek yang terlihat dalam gambar.
9. **90 Derajat Rotation:** Gambar akan diputar 90 derajat untuk meningkatkan variasi sudut pandang gambar.

Dengan menggunakan Roboflow, semua augmentasi ini diterapkan secara otomatis dan sangat membantu dalam memperkaya dataset dan mencegah overfitting selama pelatihan model.


# Visualisasi Data Gambar
Pada tahap ini, kami memvisualisasikan beberapa gambar dari dataset untuk mendapatkan gambaran yang lebih baik mengenai kelas-kelas yang ada dalam dataset.


### Teknologi yang Digunakan

### <summary><strong>Tools:</strong></summary>
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

- **Confusion matrix** digunakan untuk mengukur akurasi model, dan pengujian dilakukan menggunakan **Jupyter Notebook** / **Google Colab** dan **Visual Studio Code** sebagai teks editor utama.
- **Python**: Bahasa pemrograman utama untuk pengembangan model.
- **TensorFlow**: Framework untuk membangun model CNN.
- **OpenCV / Roboflow**: Digunakan untuk pemrosesan citra dan augmentasi gambar.
- **Matplotlib**: Untuk visualisasi hasil dan evaluasi model.

---

### Hasil 

- **Preprocessing**: Tahapan ini mengolah citra untuk mempermudah algoritma CNN dan SVM dalam proses training, dengan menggunakan augmentasi data seperti rescale, rotate, zoom, dan flip.
- **Pelatihan**: Data latih digunakan untuk mengajari model mengenali ciri-ciri dari setiap jenis penyakit melalui proses iteratif.
- **Pengujian**: Model yang telah dilatih diuji dengan dataset uji untuk mengukur akurasi dan performanya dalam mendeteksi penyakit.
- **Evaluasi** -> Coming Soon
  
---

Dengan adanya sistem ini, diharapkan proses diagnosis penyakit tanaman jagung dapat dilakukan lebih cepat dan efisien.

## License

This project is licensed under the [MIT License](LICENSE).
