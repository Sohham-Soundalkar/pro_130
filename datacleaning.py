import pandas as pd
import csv

df = pd.read_csv('total_stars.csv')
print(df.shape)

df.columns

df.drop(['Unnamed: 0', 'Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1', 'Luminosity'], axis=1, inplace=True)

final_data = df.dropna()
final_data