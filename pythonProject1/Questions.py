import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('C:\\Users\\Goabaone\\Downloads\\murder_2015.csv')
print(df.head())
sumMurders = df['2014_murders'] + df['2015_murders']
df.insert(5, 'Sum', sumMurders)
print(df)
topFive = df.nlargest(5, 'Sum')
for value in topFive['state']:
    print(value)
# another way ↓
# topFive = df.sort_values(by=['Sum'], ascending=False).head()
# print(topFive[['state']])

x = df['state']
y = df['Sum']
plt.title('Murders')
plt.scatter(x, y, c='blue', marker='x')
plt.xlabel('States')
plt.xticks(rotation=90)
plt.ylabel('2014 - 2015 Murders')
plt.show()
