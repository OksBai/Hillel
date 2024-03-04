import pandas as pd

data = pd.read_csv('data.csv')
data.drop(columns=['Age'], inplace=True)
data.to_excel('data.xlsx', index=False)
print("The data was successfully written to the file 'data.xlsx'.")
