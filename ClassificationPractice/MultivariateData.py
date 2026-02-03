import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Load dataset
dataset = pd.read_csv("Amna-AI-Course-Bin/multivariate+gait+data/gait.csv")
dataset.dropna(inplace=True)

# Features
X = dataset[['subject','condition','replication','leg','joint','time']]

# Target (categorical) -> bin angles into 3 classes
kb = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='quantile')
y = kb.fit_transform(dataset[['angle']]).astype(int).ravel()  # 0,1,2

print("Class distribution:", pd.Series(y).value_counts())

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Models
logistic_regression = LogisticRegression(max_iter=1000)
svm = SVC()
tree = DecisionTreeClassifier(random_state=42)

# Train models
logistic_regression.fit(X_train, y_train)
svm.fit(X_train, y_train)
tree.fit(X_train, y_train)

# Predictions
models = {
    "Logistic Regression": logistic_regression,
    "SVM": svm,
    "Decision Tree": tree
}

for name, model in models.items():
    preds = model.predict(X_test)
    print(f"\n{name} Classification Report:")
    print(classification_report(y_test, preds))
