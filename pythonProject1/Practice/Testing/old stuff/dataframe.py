import pandas as pd

data = {
    'StudentID': range(1, 16),
    'Name': ['Bob', 'Steven', 'Grace', 'Lance', 'Jessie', 'Isabella', 'Yuta', 'Saki',
             'Rudy', 'Walter', 'Missy', 'Angel', 'Trudy', 'Ruth', 'Ethan'],
    'Major': ['CS', 'Math', 'Eng', 'CS', 'CS', 'Eng', 'CS', 'Math', 'Math', 'CS',
              'Eng', 'CS', 'Eng', 'Math', 'Eng'],
    'MidtermScore': [78, 94, 59, 93, 50, None, 67, None, 49, None, 58, 92, 78, 98, 86],
    'FinalScore': [80, 90, None, 89, 55, 76, 70, 74, 50, None, 49, 55, 95, 80, 95],
    'AttendanceRate': [90, 80, 94, 85, 67, 89, 75, 80, 58, 94, 49, 69, 49, 79, 94]
}

df = pd.DataFrame(data)

df.to_csv('student_grades.csv', index=False)

missing_data = df[df.isnull().any(axis=1)]
print(missing_data)

median_term = df['MidtermScore'].median()
df['MidtermScore'].fillna(median_term, inplace=True)

avg_final = df[df['FinalScore']>85]['FinalScore'].mean()
df['FinalScore'].fillna(avg_final, inplace=True)

df['TotalScore'] = df['MidtermScore'] * 0.4 + df['FinalScore'] * 0.6

df.loc[df['Major'] == 'CS', 'AttendanceRate'] = df.loc[df['Major'] == 'CS', 'AttendanceRate'].apply(lambda x: min(x + 5, 100))