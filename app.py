from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Konfigurasi Flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.secret_key = 'your_secret_key'

# Load model
MODEL_PATH = 'Model/Model_CNN_256px.keras'
model = load_model(MODEL_PATH)

# Label kelas
class_labels = {0: 'Bercak', 1: 'Hawar', 2: 'Karat', 3: 'Sehat'}

def predict_image(model, img_path):
    # Load image dan ubah ukuran agar sesuai dengan input model
    img = image.load_img(img_path, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalisasi

    # Prediksi
    prediction = model.predict(img_array)
    predicted_index = np.argmax(prediction)
    return predicted_index, prediction[0]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Cek apakah ada file yang diunggah
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        if file:
            # Simpan file ke folder uploads
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Prediksi gambar
            predicted_index, probabilities = predict_image(model, filepath)
            predicted_label = class_labels[predicted_index]
            probability = probabilities[predicted_index] * 100

            # Konversi probabilitas ke dictionary
            probabilities_dict = {i: prob * 100 for i, prob in enumerate(probabilities)}

            # Tampilkan hasil
            return render_template(
                'index.html',
                image_path=filepath,
                predicted_label=predicted_label,
                probability=probability,
                probabilities_dict=probabilities_dict,
                class_labels=class_labels
            )
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
