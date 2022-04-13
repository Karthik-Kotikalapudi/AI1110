import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np
  
# defining the function
def function(x):
    return np.exp(-x)*np.sin(x)
  
# calculating its derivative
def deriv(x):
    return np.exp(-x)*np.cos(x)-np.exp(-x)*np.sin(x)
  
# defining x-axis intervals
y = np.linspace(0, np.pi)
  
# plotting the function
plt.plot(y, function(y), color='red', label="$f(x)=e^{-x} \sin x$ (Function)")
  
# plotting its derivative
plt.plot(y, deriv(y), color='green', label="$f^\prime (x)=e^{-x} \cos x-e^{-x} \sin x$ (Derivative)")

x = [np.pi/4]
y = [np.exp(-np.pi/4)*np.sin(np.pi/4)]
plt.plot(x, y, marker="o", markersize=5, markeredgecolor="black", markerfacecolor="black")

x = [np.pi/4]
y = [0]
plt.plot(x, y, marker="o", markersize=5, markeredgecolor="black", markerfacecolor="black")
plt.grid(True)  

plt.text(0.1+np.pi/4, np.exp(-np.pi/4)*np.sin(np.pi/4), "$(\\frac{\pi}{4},e^{-\\frac{\pi}{4}} \sin \\frac{\pi}{4})$")
plt.text(0.1+np.pi/4, 0, "$(\\frac{\pi}{4},0)$")
# formatting
plt.legend(loc='upper right')
plt.show()