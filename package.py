import csv
from hashmap import HashMap
import datetime
class Package:

    def __init__(self, packageID, address, city, state, zip, deadline, weight,status, truck,departureTime, deliveryTime, notes):
        self.packageID = packageID
        self.address = address
        self.city= city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.truck = truck
        self.deliveryTime= deliveryTime
        self.departureTime = departureTime
        #self.truck = truck
        self.notes = notes
    def __str__(self):
        return f"{self.packageID}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.deadline}, {self.weight}, {self.status})"
    
    
    
    # def statusUpdate(self, timeConversion):
    #     if self.deliveryTime < timeConversion:
    #         self.status = "Delivered"
    #     elif self.departureTime > timeConversion: 
    #         self.status = "En route"
    #     else:
    #         self.status = "At hub"


    def statusUpdate(self, timeConversion):
        if self.deliveryTime is not None and timeConversion is not None:
            if isinstance(self.deliveryTime, datetime.timedelta) and isinstance(timeConversion, datetime.timedelta):
                if self.deliveryTime < timeConversion:
                    self.status = "Delivered"
                elif self.departureTime > timeConversion: 
                    self.status = "En route"
                else:
                    self.status = "At hub"
            else:
                print("-------------------------------------------")
                print("ERROR: Invalid time format for comparison")
                print("-------------------------------------------")
        else:
            print("-------------------------------------------")
            print("Error: Delivery time or time conversion is None")
            print("-------------------------------------------")
    
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