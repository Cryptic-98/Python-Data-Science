import pandas as pd
# creating a dataframe
# → list1 = ['Royal', 'Simon', 'Prisha', 'Bongani', 'Sean']
data1 = {
 'Names': ['Royal', 'Peter', 'Joseph', 'Thapelo'],
 'Age': [45, 16, 78, 34],
 'Marks': [100, 45, 67, 59]
}
df = pd.DataFrame(data1)
# → print(df)
# selecting specific columns
print(df[['Names', 'Marks']])
