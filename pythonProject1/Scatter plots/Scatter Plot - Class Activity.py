import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]
a = [1, 2, 3, 4, 5]
b = [15, 18, 22, 24, 28]
plt.title('Scatter plot')
plt.scatter(x, y, c="blue", marker="v")
plt.scatter(a, b, c="red", marker="^")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.show()
