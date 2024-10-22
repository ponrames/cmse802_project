import os
import glob
import pandas as pd

# Define the input and output directories
input_dir = '/Users/rohan/Documents/MSU/Classes/CMSE  802/project/cmse802_project/data/raw'
output_dir = '/Users/rohan/Documents/MSU/Classes/CMSE  802/project/cmse802_project/data/processed/'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Get a list of all CSV files in the input directory
csv_files = glob.glob(os.path.join(input_dir, '*.csv'))

# Process each CSV file
for file_path in csv_files:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path, parse_dates=['Time Stamp'])


    # Sort the DataFrame based on 'Time Stamp'
    df = df.sort_values(by='Time Stamp')

    # Fill NaN values using forward fill
    df = df.ffill()


    # Normalize the 'Load' column
    df['normalized_load'] = (df['Load'] - df['Load'].min()) / (df['Load'].max() - df['Load'].min())

    # Create new columns for hour, day, month, and year
    df['hour'] = df['Time Stamp'].dt.hour
    df['day'] = df['Time Stamp'].dt.day
    df['month'] = df['Time Stamp'].dt.month
    df['year'] = df['Time Stamp'].dt.year

    # Create a new column for differenced load
    df['differenced_load'] = df['Load'].diff()

    # Get the base name of the file (without directory path)
    base_name = os.path.basename(file_path)

    # Define the output file path
    output_file_path = os.path.join(output_dir, base_name)

    # Save the updated DataFrame to the output file
    df.to_csv(output_file_path, index=False)

    print(f'Processed and saved: {output_file_path}')