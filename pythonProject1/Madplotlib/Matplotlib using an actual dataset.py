import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Iris.csv')
x = df['Species']
y = df['SepalLengthCm']
plt.title('Species')
plt.xlabel('Species')
plt.ylabel('Sepal Length')
plt.bar(x, y)
plt.show()
