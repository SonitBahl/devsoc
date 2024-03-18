import pandas as pd
import sys
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import joblib
import os


# Load the dataset
data = pd.read_csv(r"C:/Users/prakh/Desktop/devsoc ml model/good models/fertilizer_recommendation/fertilizer_recommendation.csv")



# Label encoding for categorical features
le_soil = LabelEncoder()
data['Soil Type'] = le_soil.fit_transform(data['Soil Type'])
le_crop = LabelEncoder()
data['Crop Type'] = le_crop.fit_transform(data['Crop Type'])

# Splitting the data into input and output variables
X = data.iloc[:, :8]
y = data.iloc[:, -1]

# Training the Decision Tree Classifier model
dtc = DecisionTreeClassifier(random_state=0)
dtc.fit(X, y)

# Get the input parameters from user input
jsonn = int(input("Enter Nitrogen content: "))
jsonp = int(input("Enter Phosphorus content: "))
jsonk = int(input("Enter Potassium content: "))
jsont = int(input("Enter Temperature: "))
jsonh = int(input("Enter Humidity: "))
jsonsm = int(input("Enter Soil moisture: "))
jsonsoil = input("Enter Soil type: ")
jsoncrop = input("Enter Crop type: ")

soil_enc = le_soil.transform([jsonsoil])[0]
crop_enc = le_crop.transform([jsoncrop])[0]

# Get the user inputs and store them in a numpy array - Urea
user_input = [[jsont, jsonh, jsonsm, soil_enc, crop_enc, jsonn, jsonk, jsonp]]

fertilizer_name = dtc.predict(user_input)

# Return the prediction as a string
print(str(fertilizer_name[0]))