import pandas as pd
from analyse import Analyzer

from data_operations import drop_unnecessary_columns, parametrize_columns


df = pd.read_csv('new_students_data.csv')
df = drop_unnecessary_columns(df)
df = parametrize_columns(df)

# start analysing
analyzer = Analyzer(df)
analyzer.analyse_bool_words_columns()
print(analyzer.bool_words_results)



columns = [
    'Liczba brakujacych przedmiotow',
    'Brakujace ECTS',
    'ECTS uznane w bieżącym semstrze'
]
