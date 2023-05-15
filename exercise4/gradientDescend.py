import numpy as np
import matplotlib.pyplot as plt

def square_fn(x):
    return x**2

def gradient(x):
    return 2 * x

def gradient_descent(square_fn, gradient, x_init, learning_rate, epsilon, max_iterations):
    x = x_init
    x_values = [x]  # Store the visited points in each epoch

    for i in range(max_iterations):
        gradient_x = gradient(x)
        x_next = x - learning_rate * gradient_x

        if np.abs(x_next - x) < epsilon:
            break

        x = x_next
        x_values.append(x)

    return x, x_values

learning_rate = 0.1
x_init = 3.5
num_iterations = 20
epsilon = 1e-6

x_optimal, x_values = gradient_descent(square_fn, gradient, x_init, learning_rate, epsilon, max_iterations=num_iterations)

# Plotting the function
x_vals = np.linspace(-4, 4, 100)
y_vals = square_fn(x_vals)
plt.plot(x_vals, y_vals, label='square_fn(x) = x^2')
plt.xlabel('x')
plt.ylabel('square_fn(x)')
plt.title('Gradient Descent')
plt.grid(True)

# Overlaying the points visited by x
x_values_vals = np.array(x_values)
y_history_vals = square_fn(x_values_vals)
plt.scatter(x_values_vals, y_history_vals, c='red', label='Epochs')
plt.legend()

plt.show()
