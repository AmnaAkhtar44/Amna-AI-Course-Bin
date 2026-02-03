import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Let's read the CSV file and package it into a DataFrame:
# Load dataset
df = pd.read_csv("Amna-AI-Course-Bin/auto-mpg[1].csv", na_values='?')

# Remove non-numeric column
df = df.drop(columns=['car name'])

# Convert to numeric
df = df.apply(pd.to_numeric, errors='coerce')

# Handle missing values
df = df.dropna()

# Correlation
print(df.corr())

#So, what's the relationship between these variables? A great way to explore relationships between variables is through Scatter plots. We'll plot the hours on the X-axis and scores on the Y-axis, and for each pair, a marker will be positioned based on their values:
df.plot.scatter(x='weight', y='mpg', title='Scatter Plot of indus and tax percentages')
plt.show()
#print('df.shape():' , df.shape())

print("df.describe():                    " , df.describe())

print(" df['weight'] :     " , df['weight'])
print("  df['mpg']   :    ", df['mpg']   )

y = df['mpg'].values.reshape(-1, 1)
X = df['weight'].values.reshape(-1, 1)

print("y :  " , y)
print("X :   " , X)

print(df['weight'].values) # [2.5 5.1 3.2 8.5 3.5 1.5 9.2 ... ]
print(df['weight'].values.shape) # (25,)

print(X.shape) # (25, 1)
print(X)      # [[2.5] [5.1]  [3.2] ... ]

SEED = 42

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = SEED)

#Now, if you print your X_train array - you'll find the study hours, and y_train contains the score percentages:

print(X_train) # [[2.7] [3.3] [5.1] [3.8] ... ]
print(y_train) # [[25] [42] [47] [35] ... ]

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print(regressor.intercept_)
print(regressor.coef_)

def calc(slope, intercept, hours):
    return slope*hours+intercept

weight = calc(regressor.coef_, regressor.intercept_, 9.5)
print(weight) # [[94.80663482]]
weight = regressor.predict([[9.5]])
print(weight) # 94.80663482
y_pred = regressor.predict(X_test)

df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score

import numpy as np

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
#We will also print the metrics results using the f string and the 2 digit precision after the comma with :.2f:

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')