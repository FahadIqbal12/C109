import plotly.figure_factory as ff
import pandas as pd
import statistics
import csv

df = pd.read_csv('data.csv')
fig= ff.create_distplot([df['Index'].tolist()],['Index'],show_hist=False)
mean = statistics.mean(df)


#fig.show()

