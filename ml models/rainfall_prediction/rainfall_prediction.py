import pandas as pd

# Load the dataset into a dataframe
df = pd.read_csv(r'C:/Users/prakh/Desktop/devsoc ml model/good models/rainfall_prediction/rainfall_in_india_1901-2015.csv')

# Define a function to predict rainfall for a given district and month
def predict_rainfall(state, month):
    # Filter the dataframe to only include rows with the given district
    state_data = df[df['SUBDIVISION'] == state]

    # Calculate the average rainfall for the given month across all the years
    avg_rainfall = state_data[month].mean()
    
    # Return the predicted rainfall for the given month
    return avg_rainfall

# Get the input parameters from user input
Jregion = input("Enter the region: ").upper()
Jmonth = input("Enter the month: ").upper()

predicted_rainfall = predict_rainfall(Jregion, Jmonth)
print(predicted_rainfall)
