
import pandas as pd
from sklearn.datasets import load_digits


digits_data = load_digits()


digits_data_return_X_y = load_digits( return_X_y= True)
print("digits_data_return_X_y :    ", digits_data_return_X_y)
print("digits_data_return_X_y[0] :    ", digits_data_return_X_y[0])
print("digits_data_return_X_y[1] :    ", digits_data_return_X_y[1])

digits_data_as_frame = load_digits(as_frame=True)
print("digits_data_as_frame", digits_data_as_frame )


# Convert data to pandas dataframe
digits_df = pd.DataFrame(digits_data.data, columns=digits_data.feature_names)

print("digits_df - dataFrame: ",digits_df)

# Add the target label
digits_df["target"] =digits_data.target


# Take a preview
print("digits_df.head() : ", digits_df.head())


print(" digits_df.info() ", digits_df.info() )

print(" digits_df.describe()  ", digits_df.describe()  )


print("digits_df.tail()" , digits_df.tail() )


from sklearn.preprocessing import StandardScaler

# Split data into features and label 
X = digits_df[digits_data.feature_names].copy()
y = digits_df["target"].copy() 

print("X:" , X)
print("y:" , y)


# Instantiate scaler and fit on features
scaler = StandardScaler()
scaler.fit(X)

# Transform features
X_scaled = scaler.transform(X.values)

# View first instance
print(X_scaled[0])


from sklearn.model_selection import train_test_split

#https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

# Split data into train and test
X_train_scaled, X_test_scaled, y_train, y_test = train_test_split(X_scaled,
                                                                  y,
                                                             train_size=.7,
                                                           random_state=25)

# Check the splits are correct
print(f"Train size: {round(len(X_train_scaled) / len(X) * 100)}% \n\
Test size: {round(len(X_test_scaled) / len(X) * 100)}%")

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

# Instnatiating the models 
logistic_regression = LogisticRegression()
svm = SVC()
tree = DecisionTreeClassifier()

# Training the models 
logistic_regression.fit(X_train_scaled, y_train)
svm.fit(X_train_scaled, y_train)
tree.fit(X_train_scaled, y_train)

# Making predictions with each model
log_reg_preds = logistic_regression.predict(X_test_scaled)
svm_preds = svm.predict(X_test_scaled)
tree_preds = tree.predict(X_test_scaled)

#https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html

from sklearn.metrics import classification_report

# Store model predictions in a dictionary
# this makes it's easier to iterate through each model
# and print the results. 
model_preds = {
    "Logistic Regression": log_reg_preds,
    "Support Vector Machine": svm_preds,
    "Decision Tree": tree_preds
}

for model, preds in model_preds.items():
    print(f"{model} Results:\n{classification_report(y_test, preds)}", sep="\n\n")