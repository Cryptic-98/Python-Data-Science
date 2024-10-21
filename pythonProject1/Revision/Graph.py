import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
months=['January', 'February', 'March', 'April', 'May', 'June']
data = np.random.randint(100, 200, 6)
data1 = np.cumsum(data)
plt.ylabel('Months')
plt.xlabel('Sales')
plt.show()