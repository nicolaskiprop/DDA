import numpy as np
import matplotlib.pyplot as plt

# Generate data
X = np.arange(0, 1, 0.01)
Y = X + np.random.normal(0, 0.2, len(X))

# Define model function
def y_hat(x, theta1, theta2):
    return theta1 * x + theta2

# Set optimal parameters
theta1 = 1.0
theta2 = 0.0

# Compute model predictions
predictions = y_hat(X, theta1, theta2)

# Plot the data and model predictions
plt.scatter(X, Y, label='Data')
plt.plot(X, predictions, color='red', label='Model Predictions')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
