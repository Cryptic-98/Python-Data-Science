import matplotlib.pyplot as plt
# when plotting a graph you need the axis
x = [2, 5, 7, 9, 12]
y = [3, 8, 9, 1, 13]
plt.title('My Line Graph')
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')
plt.plot(x, y, color='red')
plt.show()
# bar graph
x = [2, 5, 7, 9, 12]
y = [3, 8, 9, 1, 13]
plt.title('My Line Graph')
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')
plt.bar(x, y, color='red')
plt.show()
