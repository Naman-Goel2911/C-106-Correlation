import csv
import numpy as np
import plotly.express as px
import pandas as pd

df = pd.read_csv('Student Marks vs Days Present.csv')

fig = px.scatter(df, x='Days Present', y='Marks In Percentage')
fig.show()

def getDataSource(dataPath):
    marksInPercentage = []
    daysPresent = []
    with open(dataPath) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            marksInPercentage.append(float(row['Marks In Percentage']))
            daysPresent.append(float(row['Days Present']))
    
    return {'x':marksInPercentage, 'y':daysPresent}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'], dataSource['y'])
    print('Correlation between marks and percentage and days present is ', correlation[0,1])

def setup():
    dataPath = './Student Marks vs Days Present.csv'
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

setup()