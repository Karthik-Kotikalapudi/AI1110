import numpy as np
import scipy
import matplotlib.pyplot as plt
import mpmath as mp

x = np.linspace(-4,4,30)
simlen = int(1e6)
err = []

randvar = np.loadtxt('gau.dat',dtype='double')

for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) 
	err_n = np.size(err_ind) 
	err.append(err_n/simlen) 

def Q(x):
    return mp.erfc(x/mp.sqrt(2))/2
def gau_cdf(x):
	return 1-Q(x)
		
vec_gau_cdf = scipy.vectorize(gau_cdf, otypes=[float])	
plt.plot(x.T,err,'o')
plt.plot(x, vec_gau_cdf(x))
plt.grid() 
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])

plt.show()
plt.savefig('gau_cdf.pdf')
plt.savefig('gau_cdf.eps')
