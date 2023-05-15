import numpy as np
import matplotlib.pyplot as plt

def y_hat(x, theta1, theta2):
    return theta1*x+theta2

#generate data
X = np.arange(0, 1, 0.01)
Y = X + np.random.normal(0, 0.2, len(X))

# Initialize parameters
theta1 = -0.5
theta2 = 0.2

# set learning rate and max iterations
learning_rate = 0.01
Emax = 1000


# perform gradient descent
for i in range(Emax):

#    compute gradients
    grad_theta1 = np.mean((y_hat(X, theta1, theta2)-Y)*X)
    grad_theta2 = np.mean(y_hat(X, theta1, theta2)-Y)

    #Update params
    theta1 -= learning_rate * grad_theta1
    theta2 -= learning_rate * grad_theta2

# plot the data 
plt.scatter(X,Y)
#  plot the final model's predictions
predictions = y_hat(X, theta1, theta2)
plt.plot(X, predictions, color='red', label='model predictions')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Model Predictions')
plt.legend()
plt.show()
