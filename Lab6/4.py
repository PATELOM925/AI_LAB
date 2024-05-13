#create dataframe and add columns
import pandas as pd

df = pd.DataFrame(columns=['NAME', 'AGE', 'DRIVER'])
#adding data to dataframe
df.loc[0] = ['John', 25, True]
df.loc[1] = ['Smith', 30, False]
df.loc[2] = ['Sarah', 32, True]
print(df)