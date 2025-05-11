import os
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# ——— Konfigurasi dasar Flask ———
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024    # batasi upload maksimal 5MB
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'your_secret_key')

# ——— Pastikan folder uploads ada ———
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# ——— Load model Keras ———
MODEL_PATH = os.path.join(app.root_path, 'Model', 'Model_CNN_256px.keras')
model = load_model(MODEL_PATH)

# ——— Label kelas ———
class_labels = {
    0: 'Bercak',
    1: 'Hawar',
    2: 'Karat',
    3: 'Sehat'
}

# ——— Fungsi bantu untuk prediksi ———
def predict_image(model, img_path):
    img = image.load_img(img_path, target_size=(256, 256))               # resize sesuai input model :contentReference[oaicite:0]{index=0}
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0                                                   # normalisasi

    preds = model.predict(img_array)
    idx = np.argmax(preds)
    return idx, preds[0]

# ——— Route utama ———
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # cek keberadaan file pada form
        file = request.files.get('file')
        if not file or file.filename == '':
            flash('Tidak ada file yang dipilih!', 'warning')
            return redirect(request.url)

        # simpan dengan nama aman
        filename = secure_filename(file.filename)                         # lindungi dari path traversal :contentReference[oaicite:1]{index=1}
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # jalankan prediksi
        idx, probs = predict_image(model, filepath)
        label = class_labels[idx]
        confidence = float(probs[idx] * 100)

        # siapakan data probabilitas semua kelas
        probs_dict = {class_labels[i]: float(p * 100) for i, p in enumerate(probs)}

        return render_template(
            'index.html',
            image_path=url_for('static', filename=f'uploads/{filename}'),
            predicted_label=label,
            confidence=round(confidence, 2),
            probabilities=probs_dict
        )

    return render_template('index.html')

# ——— Jalankan secara lokal (debug) ———
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
