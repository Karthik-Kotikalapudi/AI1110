from numpy import random as RN

n = RN.randint(1,20)
#returns nCr value
def nCr(n, r):
    return (fact(n) / (fact(r)* fact(n - r)))
 
# Returns factorial of n
def fact(n):
    res = 1
    for i in range(2, n+1):
        res = res * i     
    return res

sum = 0
for i in range(2,n+1):
    sum += nCr(n,i)
print(sum, pow(2,n)-1-n)