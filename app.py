import os
import time
import numpy as np
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Path model
MODEL_PATH = r"D:\MATA KULIAH - DEL\SEMESTER 5\Pembelajaran Mesin\Project Machine Learning\Project Machine Learning\CornLeaf-Disease-Identification-Using-Machine-Learning\Model\model2.keras"

# Load model
model = load_model(MODEL_PATH)

# Labels untuk prediksi
labels = ['hawar', 'karat', 'bercak', 'sehat']

# Folder untuk menyimpan file upload
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Fungsi untuk memproses gambar
def preprocess_image(image_path):
    """Memproses gambar menjadi format yang sesuai dengan input model."""
    img = load_img(image_path, target_size=(256, 256))  # Ukuran sesuai model
    x = img_to_array(img)
    x = x.astype('float32') / 255.0  # Normalisasi
    x = np.expand_dims(x, axis=0)
    return x

# Fungsi untuk melakukan prediksi
def get_result(image_path):
    """Menghasilkan prediksi label dan confidence dari gambar."""
    start_time = time.time()
    x = preprocess_image(image_path)
    predictions = model.predict(x)[0]
    predicted_label = labels[np.argmax(predictions)]
    confidence = np.max(predictions) * 100
    print(f"Prediction time: {time.time() - start_time:.2f} seconds")
    return predicted_label, confidence

@app.route('/', methods=['GET'])
def index():
    """Menampilkan halaman utama."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def upload():
    """Endpoint untuk memprediksi gambar."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Simpan file
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Lakukan prediksi
    predicted_label, confidence = get_result(file_path)

    # Hapus file setelah digunakan
    os.remove(file_path)

    return jsonify({'label': predicted_label, 'confidence': f'{confidence:.2f}%'})

if __name__ == '__main__':
    app.run(debug=True)
