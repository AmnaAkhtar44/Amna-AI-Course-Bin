# =====================================
# Import required libraries
# =====================================
import pandas as pd
import numpy as np

# =====================================
# Load CSV dataset
# =====================================
dataset = pd.read_csv(
    "Amna-AI-Course-Bin/product+classification+and+clustering/pricerunner_aggregate.csv"
)

# Fix column spacing issue (VERY IMPORTANT)
dataset.columns = dataset.columns.str.strip()

print("Columns in Dataset:")
print(dataset.columns)

# =====================================
# Select required columns
# =====================================
dataset = dataset[['Category Label', 'Merchant ID']]

print("\nDataset Info:")
print(dataset.info())

# =====================================
# Handle missing values
# =====================================
dataset.dropna(inplace=True)

# =====================================
# Features (X) and Target (y)
# =====================================
X = dataset['Category Label']   # TEXT feature
y = dataset['Merchant ID']      # Numeric label

print("\nX sample:")
print(X.head())

print("\ny sample:")
print(y.head())

# =====================================
# Convert TEXT → NUMERIC (TF-IDF)
# =====================================
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(
    stop_words='english',
    max_features=3000
)

X_vectorized = vectorizer.fit_transform(X)

print("\nTF-IDF Shape:", X_vectorized.shape)

# =====================================
# Train-Test Split
# =====================================
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.3,
    random_state=42
)

print("\nTraining samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

# =====================================
# Import ML Models
# =====================================
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

# =====================================
# Initialize Models
# =====================================
log_reg = LogisticRegression(max_iter=1000)
tree = DecisionTreeClassifier(random_state=42)

# =====================================
# Train Models
# =====================================
log_reg.fit(X_train, y_train)
tree.fit(X_train, y_train)

# =====================================
# Predictions
# =====================================
log_reg_preds = log_reg.predict(X_test)
tree_preds = tree.predict(X_test)

# =====================================
# Evaluation
# =====================================
from sklearn.metrics import classification_report

print("\n===== Logistic Regression Results =====")
print(classification_report(y_test, log_reg_preds))

print("\n===== Decision Tree Results =====")
print(classification_report(y_test, tree_preds))
