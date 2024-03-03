import csv
from hashmap import HashMap
class Package:

    def __init__(self, packageID, address, city, state, zip, deadline, weight,status):
        self.packageID = packageID
        self.address = address
        self.city= city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.deliveryTime= None
        self.departureTime = None
        #self.truck = truck
        #self.notes = notes
    def __str__(self):
        return f"{self.packageID}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.deadline}, {self.weight}, {self.status})"
    
    def statusUpdate(self, convert_timedelta):
        if self.deliveryTime < convert_timedelta:
            self.status = "Delivered"
        elif self.departureTime > convert_timedelta: 
            self.status = "En route"
        else:
            self.status = "At hub"
    
# packageHashMap = HashMap()
# def loadPackage(packageData, packageInfo):
#     for package in packageData:
#         packageID = int(package[0])
#         packageAddress = package[1]
#         packageCity = package[2]
#         packageState = package[3]
#         packageZip = package[4]
#         packageDeadLine = package[5]
#         packageWeight = package[6]
#         packageStat = "At Hub"
#         packageObj = Package(packageID, packageAddress, packageCity, packageState, packageZip, packageDeadLine, packageWeight, packageStat)
#         packageHashMap.add(packageID, packageObj)
    

            

# packageHashMap = HashMap()
# packageCSVFile = "Data/packages.csv"
# with open(packageCSVFile, encoding='utf-8-sig') as file:
#     reader= csv.reader(file, delimiter = ",")
#     for row in reader:
#         packageID, address, city, state, zip, deliveryTime, weight, notes= row[:8]
#         package = Package(packageID, address, city, state, zip, deliveryTime, weight, notes)
#         packageHashMap.add(package.packageID, package)
    
# packageHashMap.printHash()