#To calculate the volume of the figure given
import numpy as np
#input parameters
r = 7
h = 4
V1 = 2/3*np.pi*r**3
V2 = np.pi*r**2*h
V3 = 1/3*np.pi*r**2*h
#Total Volume
V = V1 + V2 + V3
print(490*np.pi,V)
