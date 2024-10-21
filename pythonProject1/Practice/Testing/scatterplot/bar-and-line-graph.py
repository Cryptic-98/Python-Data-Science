import matplotlib.pyplot as plt
import numpy as np

sales_data = np.random.randint(200, 400, 6)
cumulative_sales = np.cumsum(sales_data)
Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June']

plt.bar(Months, sales_data)
plt.plot(Months, cumulative_sales)
plt.xlabel('Months')
plt.ylabel('Sales figures')
plt.show()