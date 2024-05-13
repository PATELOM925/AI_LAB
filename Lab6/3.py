import pandas as pd 
import openpyxl as px

filename = 'excel_Data.xlsx'
df = px.load_workbook(filename)
print(df)