#Calculates derivative at the point we needed
import numpy as np
from scipy.misc import derivative
def f(x):
    return np.exp(-x)*np.sin(x)
deriv = derivative(f, np.pi/4, dx=1e-11)

print('The derivative at x = \u03C0/4 which is between 0 and \u03C0 is',deriv)
