import numpy as np

#1 denotes black and 0 denotes red
First = np.array([1]*26 + [0]*26)

Second = np.array([1]*25 + [0]*26)
N = 10000;
#First card
draw1 = np.random.choice(First, size=N)
uniq1, count1 = np.unique(draw1, return_counts=True)
arr1 = dict(zip(uniq1, count1))

#Second card
draw2 = np.random.choice(Second, size=arr1[0])
uniq2, count2 = np.unique(draw2, return_counts=True)
arr2 = dict(zip(uniq2, count2))

print("Practical probability is",arr2[0]/N)