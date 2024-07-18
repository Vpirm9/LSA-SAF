"""
Name: Data_preparation.py
Description: This code merges Evapotranspiration measurements from locations
Bilje, Novo mesto and Maribor into one csv file.
It also renames the columns from Slovenan language to English. 
Entries are also sorted by location and time. Raw measurements can be downloaded from
https://meteo.arso.gov.si/met/sl/agromet/data/arhiv_etp/.

Author: Vid Primožič
Date: 22.4.2024
"""

import pandas as pd

# Load each CSV file into a separate DataFrame
df1 = pd.read_csv('Bilje.csv', sep='\t')
df1['name']='Bilje'

df2 = pd.read_csv('Maribor_-_letlisce.csv', sep='\t')
df2['name']='Maribor'

df3 = pd.read_csv('Novo_mesto.csv', sep='\t')
df3['name']='Novo mesto'


# Combine the DataFrames into a single DataFrame
combined_df = pd.concat([df1, df2, df3], ignore_index=True)

# Rename columns
combined_df.rename(columns={'leto': 'year', 'mesec': 'month', 'dan': 'day', 'Evapotranspiracija' : 'ET0'}, inplace=True)

# Combine year, month, and day columns into a single 'date' column
combined_df['date']=pd.to_datetime(combined_df[['year', 'month', 'day']])

# Drop the individual year, month, and day columns
combined_df.drop(['day', 'month', 'year', 'Padavine'], axis=1, inplace=True)

# Reorder columns as per your requirement
combined_df = combined_df[['name', 'date', 'ET0']]

#Filter df
df_filtered = combined_df[(combined_df['date'] >= '2020-01-01') & (combined_df['date'] <= '2023-12-31')]

# Export to csv
df_filtered.to_csv("ET_PM.csv", index=False)

# Print the resulting DataFrame
print(df_filtered)
