import numpy as np

def F(x):
    if(x[1]+x[0] == 6):
        return 1
    return 0

N = 100000

arr = np.random.randint(1,7,size=(N,2))
problist = arr.tolist()

count1 = problist.count([4,2]) + problist.count([2,4])

countlist = map(lambda x: F(x), problist)
countlist = list(countlist)
count2 = sum(countlist)

print("Practical probability is",count1/count2)