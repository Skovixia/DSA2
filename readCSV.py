import csv 

class ReadCSV:
    def __init__ (self, filePath, delimiter=','):
        self.filePath = filePath
        self.delimiter= delimiter

    def readCSV(self):
        data = []
        with open(self.filePath, encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter=self.delimiter)
            for row in reader:
                data.append(row)
        return data
    

# distCSVFile ="Data\distance.csv"
# packageCSVFile = "Data/packages.csv"
# addressCSVFile = "Data/address.csv"

# csvReadDist = ReadCSV(distCSVFile)
# csvReadPackage = ReadCSV(packageCSVFile)
# csvReadAddress = ReadCSV(addressCSVFile)

# CSVDist = csvReadDist.readCSV()
# CSVPackage = csvReadPackage.readCSV()
# CSVAddress = csvReadAddress.readCSV()
