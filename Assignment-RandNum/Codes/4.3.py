import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

x = np.linspace(-3,3,50)
x2 = np.linspace(-3,3,500) 
simlen = int(1e6) 
err = [] 
pdf = [] 
h = 6/49;
randvar = np.loadtxt('tri.dat',dtype='double')

for i in range(0,50):
	err_ind = np.nonzero(randvar < x[i])
	err_n = np.size(err_ind) 
	err.append(err_n/simlen) 

	
for i in range(0,49):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) 

def tri_pdf(x):
	if x > 0 and x < 1:
		return x
	elif x > 1 and x < 2:
		return 2 - x
	return 0
	
vec_tri_pdf = scipy.vectorize(tri_pdf, otypes=[float])

plt.plot(x[0:(50-1)].T,pdf, 'o')
plt.plot(x2, vec_tri_pdf(x2))
plt.grid() 
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])


plt.savefig('tri_pdf.pdf')
plt.savefig('tri_pdf.eps')
plt.show()
