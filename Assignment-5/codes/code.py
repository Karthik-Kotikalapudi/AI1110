import numpy as np

# array of all possible even numbers in a die
arr = np.arange(2,7,2)

#checking if 4 is in the above array
if 4 in arr: 
    print("Not mutually exclusive")
else:
    print("Mutually exclusive")
