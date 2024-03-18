import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
df = pd.read_csv(r'C:/Users/prakh/Desktop/devsoc ml model/good models/yield_prediction/crop_production_karnataka.csv')
df = df.drop(['Crop_Year'], axis=1)
X = df.drop(['Production'], axis=1)
y = df['Production']
categorical_cols = ['State_Name', 'District_Name', 'Season', 'Crop']
ohe = OneHotEncoder(handle_unknown='ignore')
ohe.fit(X[categorical_cols])

X_categorical = ohe.transform(X[categorical_cols])
X_final = np.hstack((X_categorical.toarray(), X.drop(categorical_cols, axis=1)))
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_final, y)

Jstate = input("Enter the state: ")
Jdistrict = input("Enter the district: ")
Jseason = input("Enter the season: ")
Jcrops = input("Enter the crop: ")
Jarea = float(input("Enter the area: "))

user_input = np.array([[Jstate, Jdistrict, Jseason, Jcrops, Jarea]])
user_input_categorical = ohe.transform(user_input[:, :4])
user_input_final = np.hstack((user_input_categorical.toarray(), user_input[:, 4:].astype(float)))

prediction = model.predict(user_input_final)
print("Predicted yield:", prediction[0])
