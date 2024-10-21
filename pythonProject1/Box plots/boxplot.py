import matplotlib.pyplot as plt
import numpy as np
# create a dataset
data = np.random.normal(100, 20, 100)
data2 = np.random.normal(50, 10, 100)
data3 = np.random.normal(100, 30, 100)
print(data)
box = plt.boxplot([data, data3, data2], vert=False, patch_artist=True)

colors = ['red', 'green', 'blue']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
plt.show()
