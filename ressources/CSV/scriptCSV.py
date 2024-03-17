#read out.csv with pandas
import pandas as pd

#list of headers
HEADER = ['Year', 'Artist', 'Album', 'Worldwide Sales (Est.)', 'Genre']

#read out.csv with pandas
df = pd.read_csv('ressources/CSV/Top 10 Albums By Year Album Length - Sheet1.csv')
df = df[HEADER].dropna()

#drop duplicates by column Album
df = df.drop_duplicates(subset='Album')

#keep if released after 2014
df = df[df['Year'] >= 2014]

df.to_csv('ressources/CSV/cleanedDataset.csv', sep=';', index=False)


