import matplotlib.pyplot as plt
x = [5, 7, 2, 17, 2, 9, 4, 11, 12, 9, 5]
y = [98, 87, 100, 77, 102, 76, 86, 85, 75, 90, 80]
plt.title('Scatter plot')
plt.scatter(x, y, c="green", marker="x")
plt.xlabel('X-Value')
plt.ylabel('Y-Value')
plt.show()
