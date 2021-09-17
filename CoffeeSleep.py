import pandas as pd
import csv
import plotly.express as px
import numpy as np

df = pd.read_csv('cups of coffee vs hours of sleep.csv')

fig = px.scatter(df, x='Coffee in ml', y='sleep in hours')
fig.show()

def getDataSource(dataPath):
    CupsOfCoffee = []
    HoursOfSleep = []
    with open(dataPath) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            CupsOfCoffee.append(float(row['Coffee in ml']))
            HoursOfSleep.append(float(row['sleep in hours']))
    
    return {'x':CupsOfCoffee, 'y':HoursOfSleep}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'], dataSource['y'])
    print('Correlation between cups of coffe and sleep in hours is ', correlation[0,1])

def setup():
    dataPath = './cups of coffee vs hours of sleep.csv'
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

setup()