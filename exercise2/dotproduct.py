#dot product using for loop
import sys
import numpy as np

A = [1, 2, 3]
B = [4, 5, 6]

# dot_product = 0
# for i in range(len(A)):
#     dot_product += A[i] * B[i]

# print(dot_product)

result=np.dot(A, B)
print(result)