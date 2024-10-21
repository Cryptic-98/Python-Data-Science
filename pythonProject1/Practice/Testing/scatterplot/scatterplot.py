import matplotlib.pyplot as plt
import numpy as np

study_hours = np.random.randint(1, 11, 50)
scores = np.random.randint(40, 101, 50)

above_70 = scores > 70

plt.scatter(study_hours[above_70], scores[above_70], color='red')
plt.scatter(study_hours[~above_70], scores[~above_70], color='blue')
plt.xlabel('Study Hours')
plt.ylabel('Scores')
plt.title('Study Hours and Scores')
plt.show()