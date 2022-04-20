import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#reading from excel
read = pd.read_excel("Assignment3.xlsx","Sheet1")
data = np.array(read)

#Major cause
dictionary=dict(zip(data[0],data[1]))
keys = list(dictionary.keys())
vals = list(dictionary.values())
maximum = max(data[1])
print(keys[vals.index(maximum)])

#bar graph
fig, ax = plt.subplots()
ax.bar(data[0], data[1])
plt.title('Graph depicting the survey results')
plt.xlabel('Causes')
plt.xticks(rotation=90)
plt.ylabel('Female fatality rates (%)')
mngr = plt.get_current_fig_manager()
plt.tight_layout()
plt.savefig("Figures/Figure_1.png")
plt.show()