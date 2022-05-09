import pandas as pd


data = pd.read_csv('./tickets.csv')
northbound = {}
southbound = {}
for j in range(12):
    for i in range(12):
        if i >= j:
            southbound[(data.iloc[j][0], data.iloc[i][0])] = [data.iloc[i][1+j],data.iloc[j][1+i]]
            northbound[(data.iloc[i][0], data.iloc[j][0])] = [data.iloc[i][1+j],data.iloc[j][1+i]]
print(northbound['Hsinchu', 'Nangang'])
print(southbound['Nangang', 'Yunlin'])




