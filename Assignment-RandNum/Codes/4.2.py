import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2.5,2.5,30)
simlen = int(1e6)
err = [] 

randvar = np.loadtxt('tri.dat',dtype='double')

for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i])
	err_n = np.size(err_ind) 
	err.append(err_n/simlen)

def tri_cdf(x):
	if x < 0: return 0
	elif x <= 1: return x*x/2.0
	elif x<2: return -x*x/2.0+2*x-1
	
vec_tri_cdf = scipy.vectorize(tri_cdf, otypes=[float]) 
plt.plot(x.T,err,'o')
plt.plot(x, vec_tri_cdf(x))
plt.grid() 
plt.xlabel('$x$')
plt.ylabel('$F_T(x)$')
plt.legend(["Numerical","Theory"])

plt.savefig('tri_cdf.pdf')
plt.savefig('tri_cdf.eps')
