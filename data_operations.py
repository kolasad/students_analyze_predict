from sklearn import preprocessing


def drop_unnecessary_columns(data_frame):
    data_frame.drop(columns=[
        'Numer dokumentu',
        'Student',
        'Semestr rejestracji',
        'Brakujace przedmioty',
        'Stopień zaawansowania pracy',
        'Informacje o pracach dyplomowych',
        'Osoba przyjmująca',
        'Osoba przypisana'
    ])
    return data_frame


def parametrize_columns(data_frame):
    print(data_frame.info())
    print(data_frame.melt())
    print(data_frame['Status'].value_counts())
    data_frame = data_frame[
        (data_frame['Status'] == 'Zamknięty - decyzja negatywna') |
        (data_frame['Status'] == 'Zamknięty - decyzja pozytywna')
    ]
    print(data_frame.head())
    
    le = preprocessing.LabelEncoder()
    data_frame['Status'] = le.fit_transform(data_frame["Status"])
    print(data_frame['Status'].value_counts())
    return data_frame
