import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder

# Load the dataset
df = pd.read_csv(r'C:/Users/prakh/Desktop/devsoc ml model/good models/yield_prediction/crop_production_karnataka.csv')

# Drop the Crop_Year column
df = df.drop(['Crop_Year'], axis=1)

# Separate the features and target variables
X = df.drop(['Production'], axis=1)
y = df['Production']

# Categorical columns for one-hot encoding
categorical_cols = ['State_Name', 'District_Name', 'Season', 'Crop']

# One-hot encode the categorical columns
ohe = OneHotEncoder(handle_unknown='ignore')
ohe.fit(X[categorical_cols])

# Convert categorical columns to one-hot encoding
X_categorical = ohe.transform(X[categorical_cols])

# Combine the one-hot encoded categorical columns and numerical columns
X_final = np.hstack((X_categorical.toarray(), X.drop(categorical_cols, axis=1)))

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_final, y)

# Get the input parameters from user input
Jstate = input("Enter the state: ")
Jdistrict = input("Enter the district: ")
Jseason = input("Enter the season: ")
Jcrops = input("Enter the crop: ")
Jarea = float(input("Enter the area: "))

# Convert the input to a numpy array
user_input = np.array([[Jstate, Jdistrict, Jseason, Jcrops, Jarea]])

# Convert the categorical columns to one-hot encoding
user_input_categorical = ohe.transform(user_input[:, :4])

# Combine the one-hot encoded categorical columns and numerical columns
user_input_final = np.hstack((user_input_categorical.toarray(), user_input[:, 4:].astype(float)))

# Make the prediction
prediction = model.predict(user_input_final)

# Print the prediction
print("Predicted yield:", prediction[0])
