import csv
import numpy as np

def getDataSource(data_path):
    marksinpercentage = []
    dayspresent = [] 
    with open(data_path) as csv_file:
        reader = csv.DictReader(csv_file)
        for i in reader:
            marksinpercentage.append(float(i['Marks In Percentage']))
            dayspresent.append(float(i['Days Present'])) 
    return{"x":marksinpercentage, "y":dayspresent}

def corelation(datasource):
    relation = np.corrcoef(datasource["x"], datasource["y"])
    print("Corelation between the marks and days present is:", relation[0,1])

def setup():
    data_path = "Student Marks vs Days Present.csv"
    datasource = getDataSource(data_path)
    corelation(datasource)

setup()    