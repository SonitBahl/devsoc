from flask import Flask, render_template, request
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import numpy as np

app = Flask(__name__)

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
    if label in label_encoder.classes_:
        return label_encoder.transform([label])[0]
    else:
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


@app.route('/submit', methods=['POST'])
def predict():
    # Extract form data
    input_state = request.form.get('selectedState', '').upper()
    
    print("Received state:", input_state)  # Print received state for debugging
    
    # Encode input state
    input_state_encoded = encode_label(input_state)

    # Use precalculated state average rainfall
    state_average = state_averages.get(input_state, 0.0)  # Default to 0 if state not found
    
    # Make prediction
    predicted_crop = clf.predict([[input_state_encoded, state_average]])
    
    # Render result template with predicted crop
    return render_template('result.html', crop=predicted_crop[0])

if __name__ == '__main__':
    app.run(debug=True)
