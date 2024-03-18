# app.py

from flask import Flask, render_template, request, redirect, url_for, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import json

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('model.h5')

# Load disease names from JSON file
with open('disease_names.json') as f:
    disease_data = json.load(f)
disease_names = disease_data['diseases']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/form1')
def form1():
    return render_template('form1.html')

@app.route('/disease_form')
def disease_form():
    return render_template('disease.html')

@app.route('/submit', methods=['POST'])
def predict():
    # Extract form data and perform prediction logic for crop recommendation
    # Redirect to the result page or any other page after crop prediction
    return redirect(url_for('result_page'))

@app.route('/submit_disease', methods=['POST'])
def predict_disease():
    # Extract form data and perform prediction logic for disease detection
    # Redirect to the result page or any other page after disease prediction
    return redirect(url_for('result_page'))

@app.route('/result')
def result_page():
    # Render the result template with appropriate data
    return render_template('result.html')

@app.route('/make_prediction_disease', methods=['POST'])
def make_prediction_disease():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'})
    
    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'No image selected'})
    
    try:
        # Read the image file and preprocess it
        image = Image.open(io.BytesIO(image_file.read()))
        image = image.resize((100, 100))  # Resize image to match model input shape
        image = np.array(image) / 255.0  # Normalize pixel values
        image = np.expand_dims(image, axis=0)  # Add batch dimension
    except Exception as e:
        return jsonify({'error': str(e)})
    
    try:
        # Make prediction using the loaded model
        predictions = model.predict(image)
        predicted_class = np.argmax(predictions)
        if predicted_class < len(disease_names):
            predicted_disease = disease_names[predicted_class]
            return jsonify({'predicted_disease': predicted_disease})
        else:
            return jsonify({'error': 'Invalid predicted class index'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
