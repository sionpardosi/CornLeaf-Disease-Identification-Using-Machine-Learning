import os
import numpy as np
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

app = Flask(__name__)

# Folder untuk mengunggah file
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Daftar model dan path-nya
model_paths = {
    "custom_256": "CNN_256x256.keras",
    "custom_128": "CNN_128x128.keras",
    "densenet_256": "DenseNet121_256x256.keras",
    "densenet_128": "DenseNet121_128x128.keras",
}

labels = {0: 'Bercak', 1: 'Hawar', 2: 'Karat', 3: 'Sehat'}

# Fungsi untuk mengecek ekstensi file
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Fungsi prediksi (dengan logika yang berbeda berdasarkan model)
# def get_result(image_path, model_name):
#     if model_name in ["custom_256", "densenet_256"]:
#         img = load_img(image_path, target_size=(256, 256))
#     elif model_name in ["custom_128", "densenet_128"]:
#         img = load_img(image_path, target_size=(128, 128))
#     else:
#         raise ValueError("Invalid model name")

#     img_array = img_to_array(img) / 255.0
#     img_array = np.expand_dims(img_array, axis=0)
    
#     model = load_model(model_paths[model_name])  # Load model sesuai pilihan
#     predictions = model.predict(img_array)[0]
#     predicted_label = labels[np.argmax(predictions)]
#     return predicted_label

# Fungsi prediksi (dengan logika yang berbeda berdasarkan model)
def get_result(image_path, model_name):
    if model_name in ["custom_256", "densenet_256"]:
        img = load_img(image_path, target_size=(256, 256))
    elif model_name in ["custom_128", "densenet_128"]:
        img = load_img(image_path, target_size=(128, 128))
    else:
        raise ValueError("Invalid model name")

    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    model = load_model(model_paths[model_name])  # Load model sesuai pilihan
    predictions = model.predict(img_array)[0]
    
    # Mengambil label dengan probabilitas tertinggi
    predicted_label_index = np.argmax(predictions)
    predicted_label = labels[predicted_label_index]
    
    # Menghitung persentase untuk setiap kelas
    class_probabilities = {labels[i]: f"{predictions[i]*100:.2f}%" for i in range(len(predictions))}
    
    return predicted_label, class_probabilities


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'file' not in request.files or 'model' not in request.form:
#         return jsonify({'error': 'No file or model selected'})
    
#     file = request.files['file']
#     model_name = request.form['model']

#     if file.filename == '':
#         return jsonify({'error': 'No selected file'})
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(file_path)

#         try:
#             predicted_label = get_result(file_path, model_name)
#         except ValueError as e:
#             return jsonify({'error': str(e)})
        
#         return jsonify({'result': predicted_label})
#     return jsonify({'error': 'Invalid file format'})

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files or 'model' not in request.form:
        return jsonify({'error': 'No file or model selected'})
    
    file = request.files['file']
    model_name = request.form['model']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        try:
            predicted_label, class_probabilities = get_result(file_path, model_name)
        except ValueError as e:
            return jsonify({'error': str(e)})
        
        return jsonify({
            'result': predicted_label,
            'class_probabilities': class_probabilities
        })
    return jsonify({'error': 'Invalid file format'})


if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
