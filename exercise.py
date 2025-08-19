import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# 1) Load dataset
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# 2) Keep only mean radius and mean texture
X = df[['mean radius', 'mean texture']]
y = df['target']  # 0 = malignant, 1 = benign

print("Data sample:\n", X.head())
print("\nTarget sample:\n", y.head())

# 3) Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4) Train a supervised model (Logistic Regression)
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

# 5) Ask user for input values
mean_radius = float(input("Enter mean radius (~6 to ~29): "))
mean_texture = float(input("Enter mean texture (~9 to ~40): "))

# 6) Predict cancerous or not
pred = clf.predict([[mean_radius, mean_texture]])[0]
pred_label = "Benign (not cancerous)" if pred == 1 else "Malignant (cancerous)"

# 7) Output
print("\nPredicted state:", pred_label)
print("Model accuracy on test set:", clf.score(X_test, y_test))