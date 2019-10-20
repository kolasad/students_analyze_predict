import seaborn
import matplotlib.pyplot as plt
import pandas as pd


class Analyzer:
    def __init__(self, data_frame):
        self.df = data_frame
        self.bool_words_results = []

    def analyse_bool_words_columns(self):
        columns = [
            'Słowo prac lub work w uzasadnieniu',
            'Słowo obiecuję lub promise w uzasadnieniu',
            'Słowo rodzin lub famil w uzasadnieniu'
        ]
        for index, column in enumerate(columns, start=1):
            plt.subplot(3, 3, index)
            seaborn.heatmap(pd.crosstab(self.df['Status'], self.df[column], normalize='columns'))
            self.bool_words_results.append(column)

        plt.tight_layout()
        plt.show()
