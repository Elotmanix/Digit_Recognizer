import numpy as np
import joblib
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Fetch the MNIST dataset
X, y = fetch_openml('mnist_784', version=1, return_X_y=True)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create and train the Random Forest Classifier
clf = RandomForestClassifier(n_jobs=-1)
clf.fit(X_train, y_train)

# Evaluate the model's performance
accuracy = clf.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.4f}")  # Format accuracy with 4 decimal places

# Save the trained model
joblib.dump(clf, 'mnist_model.pkl')

print("Model trained and saved as mnist_model.pkl")