from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the pre-trained model and other necessary data
# Load the pre-trained model
clf = joblib.load('decision_tree_model.joblib')

# Load the label encoder
try:
    label_encoder = joblib.load('label_encoder.joblib')
except FileNotFoundError:
    label_encoder = LabelEncoder()  # Create a new label encoder if file not found

# Load the state averages
state_averages = {}

try:
    loaded_state_averages = joblib.load('state_average.joblib')
    if isinstance(loaded_state_averages, dict):
        state_averages = loaded_state_averages
    else:
        raise ValueError("State averages should be loaded as a dictionary.")
except FileNotFoundError:
    print("State average file not found.")
except Exception as e:
    print("Error loading state averages:", e)

# Function to encode labels, handling unseen labels
def encode_label(label):
    global label_encoder
    try:
        return label_encoder.transform([label])[0]
    except ValueError:
        # Fit label encoder with the new label
        if label not in label_encoder.classes_:
            label_encoder.fit([label])
        return label_encoder.transform([label])[0]

# Function to decode encoded labels
def decode_label(encoded_label):
    return label_encoder.inverse_transform([encoded_label])[0]

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

if __name__ == '__main__':
    app.run(debug=True)
