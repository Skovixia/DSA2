import csv 

#this file reads all the CSVs in one place

#class with general functions for reading csvs
class ReadCSV:
    def __init__ (self, filePath, delimiter=','):
        self.filePath = filePath
        self.delimiter= delimiter

    #actrual csv reader
    def readCSV(self):
        data = []
        with open(self.filePath, encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter=self.delimiter)
            for row in reader:
                data.append(row)
        return data
    

distCSVFile = "Data/distance.csv"
packageCSVFile = "Data/packages.csv"
locationsCSVFile = "Data/locations.csv"

csvReadDist = ReadCSV(distCSVFile)
csvReadPackage = ReadCSV(packageCSVFile)
csvReadLocations = ReadCSV(locationsCSVFile)

CSVDist = csvReadDist.readCSV()
CSVPackage = csvReadPackage.readCSV()
CSVLocations = csvReadLocations.readCSV()