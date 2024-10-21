import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(100, 10, 50)
data2 = np.random.normal(80, 20, 100)
data3 = np.random.normal(50, 5, 25)
box = plt.boxplot([data, data2, data3], vert=False, patch_artist=True)

colors = ['red', 'green', 'blue']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
plt.show()