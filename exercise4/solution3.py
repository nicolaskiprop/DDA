import numpy as np
import matplotlib.pyplot as plt
from mpi4py import MPI

def y_hat(x, theta1, theta2):
    return theta1 * x + theta2

# Generate data
X = np.arange(0, 1, 0.01)
Y = X + np.random.normal(0, 0.2, len(X))

# Set the desired optimal parameters
desiredParam1 = 1.0
desiredParam2 = 0.0

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
ranksSize = comm.Get_size()

# Partition the data
samples = len(X) // ranksSize
start= rank * samples
end = start+ samples
varX = X[start:end]
varY = Y[start:end]

# Initialize parameters
theta1 = -0.5
theta2 = 0.2

# Set learning rate and max iterations
learning_rate = 0.01
Emax = 1000  # Increase the max iterations

# Perform gradient descent
for i in range(Emax):

    # Compute gradients locally
    gradientTheta1 = np.mean((y_hat(varX, theta1, theta2) - varY) * varX)
    gradientTheta2 = np.mean(y_hat(varX, theta1, theta2) - varY)

    # Sum gradients across ranks
    gradientTheta1_sum = comm.allreduce(gradientTheta1, op=MPI.SUM)
    gradientTheta2_sum = comm.allreduce(gradientTheta2, op=MPI.SUM)

    # Update parameters
    theta1 -= learning_rate * gradientTheta1_sum
    theta2 -= learning_rate * gradientTheta2_sum

    # Share the updated parameters with ranks
    comm.Bcast([theta1, MPI.DOUBLE], root=0)
    comm.Bcast([theta2, MPI.DOUBLE], root=0)

    # Check convergence
    if np.abs(theta1 - desiredParam1) < 1e-6 and np.abs(theta2 - desiredParam2) < 1e-6:
        break

# Gather the final model parameters to rank 0
finalTheta1 = comm.gather(theta1, root=0)
finalTheta2 = comm.gather(theta2, root=0)

# Plot the data
if rank == 0:
    plt.scatter(X, Y)

    # Plot the final model's predictions
    if len(finalTheta1) > 0 and len(finalTheta2) > 0:
        lastTheta1 = finalTheta1[-1]
        lastTheta2 = finalTheta2[-1]
        predictions = y_hat(X, lastTheta1, lastTheta2)
        plt.plot(X, predictions, color='red')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Model Predictions')
    plt.legend()
    plt.show()
