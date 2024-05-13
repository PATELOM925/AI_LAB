import pandas as pd

csv = 'Pantry.csv'
df = pd.read_csv(csv)
print(df.head())
print(df.describe())



