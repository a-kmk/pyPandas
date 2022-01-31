# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd;


#Other formats
# excel format
#df_xlsx = pd.read_excel('pokemon_data.xlsx')

#tab separated file
#df = pd.read_csv('pokemon_data.txt', delimiter='\t')

# Read data functions
def printColumns(df):
    print('columns:')
    print(df.columns) #Getting headers

    #print first 10 names
    print(df['Name'][0:10])

    #print specific columns
    print(df[['Name', 'Type 1', 'HP']])

def printRows(df):
    #print(df.iloc[0:5])
    for index, row in df.iterrows():
        print(index,row['Name'])

def printFirePokemon(df):
    print(df.loc[df['Type 1'] == "Fire"])

def printDatasetStats(df):
    print(df.describe)

def sortDataByName(df):
    print(df.sort_values('Name'))
    #for reverse alphabetical
    #print(df.sort_values('Name', ascending=False))
    #two columns at once, first one is asc, 2nd is desc
    #print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))

# Make changes to the data
def sumStatsIntoNewCol(df):
    df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

    #to drop the column total
    #df = df.drop(columns=['Total'])

    #another way to add  the column, axis=1 adds horizontally, axis=0 adds vertically
    #df['Total'] = df.iloc[:,4:10].sum(axis=1)

    #reorder total to be closer to the LHS
    cols = list(df.columns)
    df = df[cols[0:4] + [cols[-1]] + cols[4:12]] # this just changes the visual aspect

def saveDataToFile(df):
    df.to_csv('modified.csv', index=False) #index=false removes the index values
    #Excel option
    #df.to_excel('modified.xlsx', index=False)

    #tab-separated file
    #df.to_csv('modified.txt', index=False, sep='\t')

df = pd.read_csv('pokemon_data.csv')

#printColumns(df)
#printRows(df)
#printFirePokemon(df)
#sortDataByName(df)
sumStatsIntoNewCol(df)

df.to_csv('modified.csv', index=False) #index=false removes the index values
#print(df.head(3))
#print(df.tail(3))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
