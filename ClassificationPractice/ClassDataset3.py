# =====================================
# Import required libraries
# =====================================
import pandas as pd


# =====================================
# Load CSV dataset
# =====================================
dataset = pd.read_csv("Amna-AI-Course-Bin/predict+students+dropout+and+academic+success/data.csv" , delimiter = ';')   # <-- change path if needed

print("Dataset Head:")
print(dataset.head())


# =====================================
# Select required columns
# =====================================
dataset = dataset[['Target', 'Marital status']]

print("\nDataset Info:")
print(dataset.info())


# =====================================
# Handle missing values
# =====================================
dataset.dropna(inplace=True)


# =====================================
# Take preview
# =====================================
print("\nDataset Head:")
print(dataset.head())

print("\nDataset Tail:")
print(dataset.tail())


# =====================================
# Split data into features and label
# =====================================
X = dataset['Target'].copy()     # Feature (TEXT)
y = dataset['Marital status'].copy()    # Target (1–5)

print("\nX (Target):")
print(X.head())

print("\ny (Marital status):")
print(y.head())


# =====================================
# Convert TEXT into numerical form
# =====================================
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(
    stop_words='english',
    max_features=5000
)

X_vectorized = vectorizer.fit_transform(X)

print("\nText converted to numeric matrix")
print("Shape:", X_vectorized.shape)


# =====================================
# Train-Test Split
# =====================================
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    train_size=0.7,
    random_state=25
)

print(f"\nTrain size: {round(X_train.shape[0] / X_vectorized.shape[0] * 100)}%")
print(f"Test size: {round(X_test.shape[0] / X_vectorized.shape[0] * 100)}%")



# =====================================
# Import ML models
# =====================================
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


# =====================================
# Instantiate models
# =====================================
logistic_regression = LogisticRegression(max_iter=1000)
svm = SVC()
tree = DecisionTreeClassifier(random_state=25)


# =====================================
# Train models
# =====================================
logistic_regression.fit(X_train, y_train)
svm.fit(X_train, y_train)
tree.fit(X_train, y_train)


# =====================================
# Make predictions
# =====================================
log_reg_preds = logistic_regression.predict(X_test)
svm_preds = svm.predict(X_test)
tree_preds = tree.predict(X_test)


# =====================================
# Model Evaluation
# =====================================
from sklearn.metrics import classification_report

model_preds = {
    "Logistic Regression": log_reg_preds,
    "Support Vector Machine": svm_preds,
    "Decision Tree": tree_preds
}

for model, preds in model_preds.items():
    print(f"\n{model} Results:")
    print(classification_report(y_test, preds))
