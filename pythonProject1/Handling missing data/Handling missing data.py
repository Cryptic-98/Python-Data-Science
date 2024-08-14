import pandas as pd
import numpy as np
myDictionary = {
    'First Score': [100, 90, np.nan, 95],
    'Second Score': [30, 45, 50, np.nan],
    'Third Score': [np.nan, 40, 80, 78]
}
# creating a dataset
df = pd.DataFrame(myDictionary)
# print(df.isnull()) ← handling missing data
print(df.fillna('Null'))
