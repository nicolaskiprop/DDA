import numpy as np
import matplotlib.pyplot as plt

# Load data X and Y
X = np.arange(0, 1, 0.01)
Y = X + np.random.normal(0, 0.2, len(X))

# Define model function
def y_hat(x, theta1, theta2):
    return theta1 * x + theta2

# Define loss function
def loss(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

# Define gradients of all functions
def gradient_theta1(y_true, x, theta1, theta2):
    return np.mean(2 * x * (y_pred - y_true))

def gradient_theta2(y_true, x, theta1, theta2):
    return np.mean(2 * (y_pred - y_true))

# Set parameters
learning_rate = 0.01
emax = 5
theta1 = -0.5
theta2 = 0.2

# Optimization loop
for i in range(emax):
    # Compute predictions
    y_pred = y_hat(X, theta1, theta2)

    # Compute gradients
    grad_theta1 = gradient_theta1(Y, X, theta1, theta2)
    grad_theta2 = gradient_theta2(Y, X, theta1, theta2)

    # Update parameters
    theta1 -= learning_rate * grad_theta1
    theta2 -= learning_rate * grad_theta2

# Print optimized parameters
print("Optimized theta1:", theta1)
print("Optimized theta2:", theta2)

# Plot the data and model predictions
plt.scatter(X, Y, label='Data')
plt.plot(X, y_hat(X, theta1, theta2), color='red', label='Model Predictions')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
