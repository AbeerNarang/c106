import csv
import numpy as np

def getDataSource(data_path):
    cupsofcoffee = []
    hoursofsleep = []
    with open(data_path) as csv_file:
        reader = csv.DictReader(csv_file)
        for i in reader:
            cupsofcoffee.append(float(i["Coffee in ml"]))
            hoursofsleep.append(float(i["sleep in hours"]))
    return{"x":cupsofcoffee, "y":hoursofsleep}        

def corelation(datasource):
    relation = np.corrcoef(datasource["x"], datasource["y"])
    print("Corelation between the cups of coffee and the hours of sleep is: ", relation[0,1])

def setup():
    data_path = "cups of coffee vs hours of sleep.csv"
    datasource = getDataSource(data_path)
    corelation(datasource)

setup()    