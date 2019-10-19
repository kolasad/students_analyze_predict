import pandas as pd

from data_operations import drop_unnecessary_columns, parametrize_columns


df = pd.read_csv('new_students_data.csv')
df = drop_unnecessary_columns(df)
df = parametrize_columns(df)
