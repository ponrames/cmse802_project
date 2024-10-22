import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error

# Load the CSV file into a DataFrame
file_path = '/Users/rohan/Documents/MSU/Classes/CMSE  802/project/cmse802_project/data/raw/GENESE.csv'
df = pd.read_csv(file_path, parse_dates=['Time Stamp']).dropna()

# Reverse the DataFrame
df = df.iloc[::-1]

# Set 'Time Stamp' as the index
df.set_index('Time Stamp', inplace=True)

# Perform time series split
train_size = len(df)-144
train, test = df.iloc[:train_size], df.iloc[train_size:]

# Fit a SARIMA model to the training data
# (p, d, q) x (P, D, Q, s) parameters
model = SARIMAX(train['Load'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 288))  # Example parameters
model_fit = model.fit(disp=False)

# Make predictions on the testing data
predictions = model_fit.forecast(steps=len(test))

# Evaluate the model's performance
mse = mean_squared_error(test['Load'], predictions)
print(f'Mean Squared Error: {mse}')

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(train.index, train['Load'], label='Training Data')
plt.plot(test.index, test['Load'], label='Testing Data')
plt.plot(test.index, predictions, label='Predictions', color='red')
plt.title('SARIMA Model - Load Forecasting')
plt.xlabel('Time')
plt.ylabel('Load')
plt.legend()
plt.show()