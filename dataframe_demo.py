"""
Aaron Gold
April 22, 2023
This program demonstrates basics of using DataFrames in Python
"""

import pandas as pd


df = pd.read_csv('SP500_Constituents.csv', index_col='Symbol')
df.drop("SEC filings", axis="columns", inplace=True)
df[['City', 'State']] = df["Headquarters Location"].str.split(', ', expand=True, n=1)
print(df[df["Date first added"].isnull()])
df_missingFounded = df[df['Founded'].isnull()]
print(df_missingFounded)


#Cleans the data to make sure it is uniform
def initialYear(date):
    if not isinstance(date, str):
        result = ""
    elif len(date) < 4:
        result = ""
    else:
        result = date[:4]
    return result

df['Year first added'] = df['Date first added'].apply(initialYear)
df.head(60)

df['Year founded'] = df['Founded'].apply(initialYear)
print(df.head(60))
