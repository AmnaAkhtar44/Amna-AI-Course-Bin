# -------------------------------
# Load libraries
# -------------------------------
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus


# -------------------------------
# Load dataset
# -------------------------------
col_names = ['TV', 'Radio', 'Newspaper', 'Sales']
pima = pd.read_csv(
    "Amna-AI-Course-Bin/advertising.csv",
    header=1,
    names=col_names
)


# -------------------------------
# CREATE DISCRETE TARGET LABEL
# (Required for Classifier)
# -------------------------------
pima['y_label'] = (pima['Sales'] > pima['Sales'].mean()).astype(int)


# -------------------------------
# Split dataset into features and target
# -------------------------------
feature_cols = ['TV', 'Radio', 'Newspaper']
X = pima[feature_cols]        # Features
y = pima['y_label']           # Target (DISCRETE)


# -------------------------------
# Train-test split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)


# -------------------------------
# Decision Tree Classifier (Gini)
# -------------------------------
clf = DecisionTreeClassifier(random_state=1)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("Accuracy (Gini):", metrics.accuracy_score(y_test, y_pred))


# -------------------------------
# Visualize Tree (Version 1)
# -------------------------------
dot_data = StringIO()
export_graphviz(
    clf,
    out_file=dot_data,
    filled=True,
    rounded=True,
    feature_names=feature_cols,
    class_names=['Low Sales', 'High Sales']
)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('advertisingV1.png')
Image(graph.create_png())


# -------------------------------
# Decision Tree Classifier (Entropy + max_depth)
# -------------------------------
clf = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=3,
    random_state=1
)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("Accuracy (Entropy, depth=3):",
      metrics.accuracy_score(y_test, y_pred))


# -------------------------------
# Visualize Tree (Version 2)
# -------------------------------
dot_data = StringIO()
export_graphviz(
    clf,
    out_file=dot_data,
    filled=True,
    rounded=True,
    feature_names=feature_cols,
    class_names=['Low Sales', 'High Sales']
)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('advertisingV2.png')
Image(graph.create_png())


input("Wait for me...")
