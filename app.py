from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

app = Flask(__name__)

# Load the pre-trained model
clf = joblib.load('devsoc/decision_tree_model.joblib')

# Load the label encoder
label_encoder = joblib.load('devsoc/label_encoder.joblib')

# Load the state averages
state_averages = joblib.load('devsoc/state_average.joblib')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def predict():
    # Extract form data
    input_state = request.form.get('state', '').upper()
    
    # Use precalculated state average rainfall
    state_average = state_averages.get(input_state, 0.0)  # Default to 0 if state not found
    
    # Encode input state
    input_state_encoded = label_encoder.transform([input_state])[0]
    
    # Make prediction
    predicted_crop = clf.predict([[input_state_encoded, state_average]])
    
    # Render result template with predicted crop
    return render_template('result.html', crop=predicted_crop[0])


if __name__ == '__main__':
    app.run(debug=True)