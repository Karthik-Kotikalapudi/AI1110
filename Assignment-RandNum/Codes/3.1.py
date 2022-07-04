import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp

x = np.linspace(-4,4,30)
simlen = int(1e6) 
err = [] 

randvar = np.loadtxt('v.dat',dtype='double')

for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) 
	err_n = np.size(err_ind) 
	err.append(err_n/simlen) 

def v_cdf(x):
	if x>0: return 1-mp.exp(-x/2.0)
	else: return 0
vec_v_cdf = scipy.vectorize(v_cdf, otypes=[float])
plt.plot(x.T,err,'o')
plt.plot(x, vec_v_cdf(x))
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_V(x)$')
plt.legend(["Numerical","Theory"])

plt.savefig('v_cdf.pdf')
plt.savefig('v_cdf.eps')
