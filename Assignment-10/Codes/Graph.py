
import numpy as np
import matplotlib.pyplot as plt


ax = plt.gca()

#Square
rectangle = plt.Rectangle((0,0), 60, 60, fc='blue',ec="black")
ax.add_patch(rectangle)

#plotting lines
x_values=[10,60]
y_values=[0,50]
plt.plot(x_values, y_values, color="black", linestyle="-")

x_values=[0,60-26.83]
y_values=[26.83,60]
plt.plot(x_values, y_values, color="black", linestyle="-")

# labeling axis
plt.xlabel("Arrival time of bus after 9AM in mins(X)")
plt.ylabel("Arrival time of train after 9AM in mins(Y)")

x = np.arange(0,60,0.1)
  
#Filling the region
a1 = x-10
a2 = x+26.83
plt.fill_between(x,a1,0, where = (x>10), color = "white")
plt.fill_between(x,a2,60, where = (x<60-26.83), color = "white")

plt.text(40,25,"X = Y + 10",rotation=45, rotation_mode='anchor')
plt.text(10,40,"Y = X + x",rotation=45, rotation_mode='anchor')
plt.text(28,38,"$X_1=1$")
plt.text(5,55,"$X_1=0,X_2=0$")
plt.text(40,5,"$X_1=0,X_2=1$")

plt.axis('scaled')

# Displaying graph
plt.show()