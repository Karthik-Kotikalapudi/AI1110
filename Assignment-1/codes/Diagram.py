import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Wedge

ax = plt.gca()

#triangle
pts = np.array([[0,4], [14,4], [7,8]])
p = Polygon(pts, closed=True, fc='white', edgecolor='black')
ax.add_patch(p)

#rectangle
rectangle = plt.Rectangle((0,0), 14, 4, fc='white', edgecolor='black')
ax.add_patch(rectangle)

#semi-circle
w = Wedge((7,0), 7, 180, 360, fc='white', edgecolor='black')
ax.add_artist(w)

#Dimensions of the figures
plt.text(14.5,2, "4 cm")
plt.text(7.5,-1.5, "Radius = 7 cm")

x1, y1 = [7,7],[4,8]
plt.plot(x1,y1,color = "black")
plt.text(7.5,6, "4 cm")

#ellipse
u=7 #x-position of the center
v=0 #y-position of the center
a=7 #semi major axis
b=0.5 #semi minor axis
t = np.linspace(0, 2*np.pi, 100)
plt.plot( u+a*np.cos(t) , v+b*np.sin(t), color='black')

v=4
t = np.linspace(0, 2*np.pi, 100)
plt.plot( u+a*np.cos(t) , v+b*np.sin(t), color='black')

#plotting center points
plt.plot(7, 0, marker="o", markersize=2.5, markeredgecolor="black", markerfacecolor="black")
plt.plot(7, 4, marker="o", markersize=2.5, markeredgecolor="black", markerfacecolor="black")

ax.set_xlim(-5, 20)
ax.set_ylim(-10, 15)

plt.savefig("../Figs/Diagram.png")
plt.show()
