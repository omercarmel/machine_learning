import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1) Read dataset from CSV
# fruits.csv should have columns: weight, sweetness, label
# Example rows:
# 130,0.80,apple
# 145,0.78,apple
# ...
df = pd.read_csv("fruits.csv")

# 2) Separate features (X) and labels (y)
X = df[["weight", "sweetness"]].values  # 2D array
y = df["label"].values                  # 1D array of 'apple'/'orange'

# 3) Choose and train model
clf = LogisticRegression()
clf.fit(X, y)

# 4) Predict a new fruit
new_fruit = np.array([[200, 0.9]])
proba = clf.predict_proba(new_fruit)
pred = clf.predict(new_fruit)[0]

print("Predicted fruit:", pred)
print("Class probabilities:", dict(zip(clf.classes_, proba[0])))

# 5) Evaluate on the training set (demo only)
train_pred = clf.predict(X)
print("Training Accuracy:", accuracy_score(y, train_pred))