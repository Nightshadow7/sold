import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression

# Generate a regression problem
X, y = make_regression(
  n_samples=100,
  n_features=2,
  n_informative=2,
  noise = 10,
  random_state=25
  )

# Visualize feature at index 1 vs target
plt.subplots(figsize=(8, 5))
plt.scatter(X[:, 1], y, marker='o')
plt.xlabel("Feature at Index 1")
plt.ylabel("Target")
plt.show()
