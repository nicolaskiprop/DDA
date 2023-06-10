
# from mpi4py import MPI

# A = [1, 2, 3]
# B = [4, 5, 6]
# C = [7, 8, 9]

# #initialize MPI
# comm = MPI.COMM_WORLD
# rank = comm.Get_rank()
# size = comm.Get_size()

# #divide workload and send to each process
# dotProduct = 0
# for i in range(rank, len(A), size):
#     dotProduct += A[i] * B[i] * C[i]    

# #sum up the results from each process
# dotProduct = comm.allreduce(dotProduct, op=MPI.SUM)

# #print the result
# if rank == 0:
#     print("The dot product is: ", dotProduct)

    
#collective communication functions
import numpy as np
from mpi4py import MPI

A = ([1, 2, 3])
B = ([4, 5, 6])
C = ([7, 8, 9])

#initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#divide workload and send to each process
dotProduct = np.dot(A, B) * C

#sum up the results from each process
dotProduct = np.empty(1, dtype=np.int)
comm.Allreduce([dotProduct, MPI.INT], [dotProduct, MPI.INT], op=MPI.SUM)

#print the result
if rank == 0:
    print("The dot product is: ", dotProduct)