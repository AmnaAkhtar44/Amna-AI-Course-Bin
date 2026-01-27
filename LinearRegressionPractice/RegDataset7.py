import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Read CSV file
df = pd.read_csv('Amna-AI-Course-Bin/housing[1].csv')

# Step 2: Convert categorical column to numeric
df = pd.get_dummies(df, columns=['ocean_proximity'], drop_first=True)

# Step 3: Convert all columns to numeric (safety)
df = df.apply(pd.to_numeric, errors='coerce')

# Step 4: Handle missing values
df = df.dropna()

# Step 5: Define Features (X) and Target (y)
X = df[['median_income']]     # SIMPLE LINEAR REGRESSION
y = df['median_house_value']

# Step 6: Peek data
print(df.head())
print("df.shape:         ", df.shape)

# Step 7: Scatter plot
df.plot.scatter(
    x='median_income',
    y='median_house_value',
    title='Scatter Plot of Median Income vs Median House Value'
)
plt.show()

# Step 8: Correlation & description
print("df.corr():        ", df.corr())
print("df.describe():    ", df.describe())

print("df['median_house_value']:", df['median_house_value'])

# Step 9: Convert to numpy arrays
X = X.values.reshape(-1, 1)
y = y.values.reshape(-1, 1)

print("X shape:", X.shape)
print("y shape:", y.shape)

SEED = 42

# Step 10: Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=SEED
)

print(X_train)
print(y_train)

# Step 11: Train Linear Regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

print("Intercept:", regressor.intercept_)
print("Coefficient:", regressor.coef_)

# Step 12: Manual prediction function
def calc(slope, intercept, income):
    return slope * income + intercept

predicted_value = calc(regressor.coef_, regressor.intercept_, 5.0)
print("Predicted house value for median_income=5:", predicted_value)

# Step 13: Predictions on test data
y_pred = regressor.predict(X_test)

df_preds = pd.DataFrame({
    'Actual': y_test.squeeze(),
    'Predicted': y_pred.squeeze()
})
print(df_preds)

# Step 14: Model evaluation
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')
