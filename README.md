# cmse802_project

## Energy Demand Spike and Load Forecast Project

## Project Overview

This project aims to develop predictive models that accurately forecast energy demand spikes, ensuring efficient energy distribution and preventing blackouts. By leveraging historical energy usage data, weather information, and other relevant factors, the models will help energy providers anticipate high-demand periods and optimize grid management.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Modeling](#modeling)
- [Results](#results)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In this project, we explore various predictive modeling techniques to forecast energy demand spikes. Energy demand can be volatile, leading to challenges in maintaining a balanced grid. By forecasting these spikes, energy providers can distribute resources efficiently and avoid costly blackouts.

### Key Objectives:
1. Develop a reliable predictive model for energy demand spikes.
2. Analyze patterns in energy consumption using historical data.
3. Test various machine learning algorithms for time series forecasting.
4. Ensure accurate demand predictions to optimize energy distribution.

## Dataset

We use **historical energy consumption data** provided by the **New York Independent System Operator (NYISO)**. This dataset includes the hourly energy load for different zones in New York state over several years.

The key features of the dataset are:
- **Time Stamp**: The date and time of the recorded energy consumption.
- **Load (MW)**: The actual energy demand in megawatts (MW) at each time point.
- **Zone**: The geographic zone within New York (e.g., NYC, Capital, North).
- **Temperature (°C)**: Historical temperature data, sourced from weather stations or external APIs, to capture the effect of weather on energy demand.

### Accessing the NYISO Data:
You can download the historical energy consumption data directly from the **NYISO** website or API:
- [NYISO Energy Data](https://www.nyiso.com/)
- Historical load data for different regions of New York can be accessed under the "Energy Market and Operations" section.
- the [Extractor Script](/data/raw/extractor.py) has the data extraction functions to generate 2 years load data


### Sample Dataset Structure:
- `Time Stamp`: Date and time of energy usage.
- `Energy Demand (MW)`: Actual energy consumption at that time.
- `Temperature (°C)`: Temperature at the time of recording.
- `Holiday Indicator`: Boolean flag for public holidays.

## Methodology

### Data Preprocessing:
1. **Handling Missing Data**: We employ various imputation techniques to deal with missing values.
2. **Feature Engineering**: Creating lag features, rolling means, and seasonal components.
3. **Normalization**: Scaling the features for better model performance.

### Model Building:
1. **Time Series Models**: SARIMA, ARIMA.
2. **Machine Learning Models**: Random Forest, XGBoost, LightGBM.
3. **Deep Learning Models**: LSTM (Long Short-Term Memory), GRU (Gated Recurrent Units).
4. **Evaluation**: Using metrics like Mean Absolute Error (MAE), Root Mean Square Error (RMSE), and Accuracy to evaluate model performance.

## Modeling

1. **SARIMA Model**:
   - Used for capturing seasonality and trend in the time series data.
   
2. **LSTM Neural Network**:
   - Used to capture long-term dependencies in the energy consumption data for better forecasts.
   
3. **XGBoost**:
   - Gradient-boosted trees model to capture non-linear relationships in the data.

### Model Evaluation:
- **Mean Absolute Error (MAE)**
- **Root Mean Square Error (RMSE)**
- **R-squared Score**

## Results

The LSTM model provided the most accurate predictions, with a low MAE and RMSE. It was able to forecast demand spikes with greater precision compared to traditional time series models.

### Key Results:
- Best model: ** Yet to be Decided**
- **MAE**: X (value)
- **RMSE**: Y (value)
- **R² Score**: Z (value)

## Technologies Used

- **Python**: Main programming language.
- **Pandas**: Data manipulation.
- **Scikit-learn**: Machine learning algorithms.
- **TensorFlow/Keras**: Deep learning models (LSTM, GRU).
- **Matplotlib & Seaborn**: Data visualization.
- **Statsmodels**: SARIMA modeling.
- **XGBoost**: Machine learning algorithm for gradient boosting.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ponrames/cmse802_project.git
   cd cmse802_project
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the dataset (e.g., from [NYISO](https://www.nyiso.com/)) and place it in the `data/` folder.


## Future Improvements

1. Incorporating additional features such as energy prices and grid congestion.
2. Experimenting with other deep learning architectures, such as Transformer models.
3. Using real-time data for continuous learning and model updating.
4. Implementing a real-time alert system for energy providers.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to discuss any changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

