import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
from pmdarima import auto_arima
import itertools
import numpy as np
 
# Load the AirPassengers dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
data = pd.read_csv(url, header=0, index_col=0, parse_dates=True)

# Visualize the data
plt.figure(figsize=(10,6))
plt.plot(data, label='Number of AirPassengers')
plt.title('Monthly Number of AirPassengers')
plt.xlabel('Date')
plt.ylabel('Passengers')
plt.legend()
plt.show()


# Split the data into training and testing sets
train_size = int(len(data) * 0.8)
train, test = data[:train_size], data[train_size:]


# Define and fit the SARIMA model
model = SARIMAX(train, 
                order=(1, 1, 1),  # p, d, q
                seasonal_order=(1, 1, 1, 12))  # P, D, Q, m

sarima_fit = model.fit(disp=False)

# Make predictions on the test set
predictions = sarima_fit.forecast(steps=len(test))

# Visualize the predictions
plt.figure(figsize=(10,6))
plt.plot(train.index, train, label='Train')
plt.plot(test.index, test, label='Test')
plt.plot(test.index, predictions, label='Predictions', color='red')
plt.title('SARIMA Model Predictions vs Actual')
plt.xlabel('Date')
plt.ylabel('Passengers')
plt.legend()
plt.show()


# Calculate the mean squared error
rmse = mean_squared_error(test, predictions)
print(f'Root Mean Squared Error: {rmse}')




# Define the p, d, q, P, D, Q, and m values to try
p = d = q = range(0, 3)  # Range for p, d, q values
P = D = Q = range(0, 3)  # Range for seasonal P, D, Q values
m = [12]  # Seasonal period for monthly data

# Generate all combinations of p, d, q, P, D, Q, m
pdq = list(itertools.product(p, d, q))
seasonal_pdq = list(itertools.product(P, D, Q, m))

# Grid search to find the best parameters
best_aic = np.inf
best_params = None
for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            model = SARIMAX(train,
                            order=param,
                            seasonal_order=param_seasonal)
            sarima_fit = model.fit(disp=False)
            aic = sarima_fit.aic
            if aic < best_aic:
                best_aic = aic
                best_params = (param, param_seasonal)
        except Exception as e:
            continue

print(f'Best SARIMA parameters: {best_params}')



# Automatically fit the best SARIMA model
auto_model = auto_arima(train,
                        seasonal=True,
                        m=12,  # Seasonal period for monthly data
                        stepwise=True,
                        suppress_warnings=True)

# Print the best found parameters
print(auto_model.summary())


"""
Best SARIMA parameters: ((1, 1, 0), (0, 2, 2, 12))
                                     SARIMAX Results                                      
==========================================================================================
Dep. Variable:                                  y   No. Observations:                  115
Model:             SARIMAX(1, 1, 0)x(0, 1, 0, 12)   Log Likelihood                -375.750
Date:                            Thu, 10 Oct 2024   AIC                            755.499
Time:                                    20:30:53   BIC                            760.749
Sample:                                01-01-1949   HQIC                           757.625
                                     - 07-01-1958                                         
Covariance Type:                              opg                                         
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1         -0.2048      0.090     -2.271      0.023      -0.382      -0.028
sigma2        92.6974     13.326      6.956      0.000      66.579     118.816
===================================================================================
Ljung-Box (L1) (Q):                   0.03   Jarque-Bera (JB):                 2.44
Prob(Q):                              0.87   Prob(JB):                         0.30
Heteroskedasticity (H):               0.96   Skew:                             0.37
Prob(H) (two-sided):                  0.92   Kurtosis:                         2.86
===================================================================================


"""