import pandas as pd

# Load the first CSV (Load Data)
load_data = pd.read_csv("data/processed/GENESE.csv")
load_data["Time Stamp"] = pd.to_datetime(load_data["Time Stamp"])  # Convert to datetime

# Downsample load data to hourly intervals using cumsum
load_data["hour"] = load_data["Time Stamp"].dt.floor("H")  # Create a new column for hourly timestamps
hourly_load_data = (
    load_data.groupby("hour")
    .agg({"Load": "sum", "normalized_load": "sum"})  # Cumulative sum for load-related columns
    .reset_index()
    .rename(columns={"hour": "Time Stamp"})  # Rename column back to match weather_data
)

# Load the second CSV (Weather Data)
weather_data = pd.read_csv("data/processed/GENESE_Weather.csv")
weather_data.rename(columns={weather_data.columns[0]: "Time Stamp"}, inplace=True)  # Rename time column
weather_data["Time Stamp"] = pd.to_datetime(weather_data["Time Stamp"])  # Convert to datetime

# Merge the datasets on hourly timestamps
combined_data = pd.merge(hourly_load_data, weather_data, on="Time Stamp", how="inner")

# Save the combined dataset to a new CSV
combined_data.to_csv("combined_data.csv", index=False)

print("Combined dataset created as 'combined_data.csv'.")
