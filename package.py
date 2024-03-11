from hashmap import HashMap
from readCSV import CSVPackage
import datetime
class Package:

    #class constructor
    def __init__(self, packageID, address, city, state, zip, deadline, weight,status, truck, departureTime, deliveryTime, notes):
        self.packageID = packageID
        self.address = address
        self.city= city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.truck = truck  #assigning a truck to each package(for debugging)
        self.deliveryTime= None #setting del time and depart time to none, will be updated when delivered
        self.departureTime = None
        self.notes = notes
    def __str__(self):
        #for interface- If not delivered yet, will display "estimated delivery"
        if self.status == "Delivered":
            deliveryLabel = "Delivery Time" 
        else:
            deliveryLabel = "Estimated Delivery Time"

        strLength = len(f"|{self.packageID}| Destination: {self.address}, {self.city}, {self.state}, {self.zip}| Deadline: {self.deadline}| Weight: {self.weight}| Truck: {self.truck}| Departure Time: {self.departureTime}| {deliveryLabel}: {self.deliveryTime}| Status: {self.status}")
        print("-" * strLength)
        return f"|{self.packageID}| Destination: {self.address}, {self.city}, {self.state}, {self.zip}| Deadline: {self.deadline}| Weight: {self.weight}| Truck: {self.truck}| Departure Time: {self.departureTime}| {deliveryLabel}: {self.deliveryTime}| Status: {self.status}"
        
    
    #for updating status based on time given in main
    def statusUpdate(self, inputTime):
        if self.departureTime is not None:
            if self.deliveryTime < inputTime:
                self.status = "Delivered"
            elif self.departureTime <= inputTime <= self.deliveryTime:
                self.status = "En route"
            else:
                self.status = "At hub"

def isUpdateTime(inputTime, hashmap):
    updateTime = datetime.timedelta(hours = 10, minutes = 20)
    if inputTime >= updateTime:
        updatePackageAddress(hashmap, 9, '410 S State St', 'Salt Lake City', 'UT', '84111')

#packageHashMap = HashMap()

#laoding each package to hashmap 
def loadPackages(packageData, hashmap):
    for package in packageData:
        packageID = int(package[0])
        packageAddress, packageCity, packageState, packageZip, packageDeadLine, packageWeight, packageNotes = package[1:8]
        packageStat = "At Hub"
        packageTruck = None
        packageDelTime= None
        packageDepartTime = None
        packageObj = Package(packageID, packageAddress, packageCity, packageState, packageZip, packageDeadLine,
                             packageWeight, packageStat, packageTruck, packageDelTime,
                             packageDepartTime, packageNotes)
        
        hashmap.add(packageID, packageObj)
        #print(f"Added package to hashmap - ID: {packageID}, Address: {packageAddress}, Status: {packageStat}")
        
#loadPackages(CSVPackage, packageHashMap)

#function for updating addresses if addresses is wrong
def updatePackageAddress(hashmap, packageID, newAddress = None, newCity = None, newState = None, newZip = None):
    # creates copy of the package object
    package = hashmap.lookup(packageID)

    updatedPackage = Package(
      packageID, newAddress,   # Updates only address fields
      newCity, newState, newZip,
      package.deadline, package.weight, package.status, package.truck, package.deliveryTime,
      package.departureTime, package.notes
      )
    hashmap.update(packageID, updatedPackage)
    return hashmap.lookup(packageID)
