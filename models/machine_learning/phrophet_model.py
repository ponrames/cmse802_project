import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
from sklearn.metrics import mean_squared_error

# Load the CSV file into a DataFrame
file_path = '/Users/rohan/Documents/MSU/Classes/CMSE  802/project/cmse802_project/data/processed/combined_data.csv'
df = pd.read_csv(file_path, parse_dates=['Time Stamp']).dropna()


df = df.sort_values(by='Time Stamp')

# Prepare the data for Prophet
df = df.rename(columns={'Time Stamp': 'ds', 'Load': 'y'})

# Perform time series split
train_size = len(df)-702
train, test = df.iloc[:train_size], df.iloc[train_size:]

# Fit the Prophet model to the training data
model = Prophet()
model.fit(train)
future = model.make_future_dataframe(periods=len(test), freq='5min')
forecast = model.predict(future)

# Calculate the rate of change for future values
forecast['rate_of_change'] = forecast['yhat'].diff()

# Set a threshold for surge prediction (adjust based on your data)
# Example: 1.4 standard deviations above the mean rate of change
threshold = forecast['rate_of_change'].mean() + 1.4 * forecast['rate_of_change'].std()

# Predict future surges: Identify points where rate of change exceeds the threshold
forecast['is_predicted_surge'] = forecast['rate_of_change'] > threshold

# Filter the future surge points
predicted_surge_points = forecast[forecast['is_predicted_surge']]

# Plot the predicted surges on the future forecast
plt.figure(figsize=(12, 6))
plt.plot(train['ds'], train['y'], label='Training Data')
plt.plot(test['ds'], test['y'], label='Testing Data')
plt.plot(test['ds'], forecast['yhat'].iloc[-len(test):], label='Predictions', color='red')

# Mark the predicted surges with orange crosses
plt.scatter(predicted_surge_points['ds'], predicted_surge_points['yhat'], color='orange', label='Predicted Surge', marker='x', s=100)

plt.title('Prophet Model - Load Forecasting with Predicted Surges')
plt.xlabel('Time')
plt.ylabel('Load')
plt.legend()

# Plot the forecast components
model.plot_components(forecast)
plt.show()


# Print out the predicted surge points for further analysis
print(predicted_surge_points[['ds', 'yhat', 'rate_of_change']])