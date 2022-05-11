import numpy as np

Bags = np.array([0]+[1])

N = 10000;

selecting_Bag = np.random.choice(Bags, size=N)
uniq, count = np.unique(selecting_Bag, return_counts=True)
arr = dict(zip(uniq, count))
ProbB1 = arr[0]
ProbB2 = arr[1]

#1 denotes black and 0 denotes red
Bag1 = np.array([1]*4 + [0]*3)
Bag2 = np.array([1]*6 + [0]*5)

#for first bag
ballcolor1 = np.random.choice(Bag1, size=N)
uniq1, count1 = np.unique(ballcolor1, return_counts=True)
arr1 = dict(zip(uniq1, count1))
ProbB1_red = arr1[0]

#for second bag
ballcolor2 = np.random.choice(Bag1, size=N)
uniq2, count2 = np.unique(ballcolor2, return_counts=True)
arr2 = dict(zip(uniq2, count2))
ProbB2_red = arr2[0]

Req_prob = (ProbB2*ProbB2_red)/(ProbB2*ProbB2_red+ProbB1*ProbB1_red)

print("Practical probability is ", Req_prob)