import pandas as pd
import numpy as np
import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model(X_train, y_train):
    classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
    classifier.fit(X_train, y_train)
    return classifier

def get_input_params():
    # n_params = 90
    # p_params = 42
    # k_params = 43
    # t_params = 21.0
    # h_params = 82.0
    # ph_params = 6.5
    # r_params = 203.0

    n_params = int(input("Enter the nitrogen content (N): "))
    p_params = int(input("Enter the phosphorus content (P): "))
    k_params = int(input("Enter the potassium content (K): "))
    t_params = float(input("Enter the temperature: "))
    h_params = float(input("Enter the humidity: "))
    ph_params = float(input("Enter the pH value: "))
    r_params = float(input("Enter the rainfall: "))
    
    return n_params, p_params, k_params, t_params, h_params, ph_params, r_params

def make_predictions(classifier, user_input):
    predictions = classifier.predict(user_input)
    return predictions

def main():
    dataset = pd.read_csv(r'C:/Users/prakh/Desktop/devsoc ml model/good models/crop_recommendation/Crop_recommendation.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=0)

    classifier = train_model(X_train, y_train)

    n_params, p_params, k_params, t_params, h_params, ph_params, r_params = get_input_params()

    user_input = np.array([[n_params, p_params, k_params, t_params, h_params, ph_params, r_params]])

    predictions = make_predictions(classifier, user_input)

    print("Predicted crop:", predictions[0])

if __name__ == "__main__":
    main()
