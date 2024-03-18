import pandas as pd
df = pd.read_csv(r'C:/Users/prakh/Desktop/devsoc ml model/good models/rainfall_prediction/rainfall_in_india_1901-2015.csv')
def predict_rainfall(state, month):
    state_data = df[df['SUBDIVISION'] == state]
    avg_rainfall = state_data[month].mean()
    return avg_rainfall

Jregion = input("Enter the region: ").upper()
Jmonth = input("Enter the month: ").upper()

predicted_rainfall = predict_rainfall(Jregion, Jmonth)
print(predicted_rainfall)
