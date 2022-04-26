import numpy as np
from numpy import random as RN 

# n_0 denotes number of orange flavoured candies
n_0 = 0
# n_1 denotes number of lemon flavoured candies. As the number is not given, let it be a number in first 100 natural numbers
n_1 = RN.randint(1,100)
N = n_0 + n_1
pr_0 = n_0/N
pr_1 = n_1/N

# Let x take any value from 1 to 100 inclusive over the size N ,
x = RN.randint(1, 100, size=N)

#Practical probabilities

x_1 = np.count_nonzero(x>0)
x_0 = N - x_1

print("Theoretical Probabilities:", pr_0, pr_1)
print("Practical Probabilities:", x_0/N, x_1/N)