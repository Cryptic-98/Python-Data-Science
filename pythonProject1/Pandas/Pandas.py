import pandas as pd
# creating pandas series
data = [10, 20, 30, 45, 56, 60, 70]
index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
my_Series = pd.Series(data, index)
print(my_Series)
grades = {
    'John': 89,
    'Sean': 70,
    'Hope': 65,
    'Nyiko': 26
}
# trying to change index from the dictionary
index2 = [1, 2, 3, 4]
my_Series = pd.Series(grades, index2)
print(my_Series)
