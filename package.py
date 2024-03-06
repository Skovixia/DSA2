from hashmap import HashMap
from readCSV import CSVPackage
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
        if self.deliveryTime < inputTime:
            self.status = "Delivered"
        elif self.departureTime <= inputTime <= self.deliveryTime:
            self.status = "En route"
        else:
            self.status = "At hub"


packageHashMap = HashMap()

#laoding each package to hashmap 
def loadPackages(packageData, hashmap):
    for package in packageData:
        packageID = int(package[0])
        packageAddress, packageCity, packageState, packageZip, packageDeadLine, packageWeight, packageNotes = package[1:8]
        packageStat = "At Hub"
        packageTruck = None
        packageDelTime= None
        packageDepartTime = None
        packageObj = Package(packageID, packageAddress, packageCity, packageState, packageZip, packageDeadLine, packageWeight, packageStat, packageTruck, packageDelTime, packageDepartTime, packageNotes)
        packageHashMap.add(packageID, packageObj)
        #print(f"Added package to hashmap - ID: {packageID}, Address: {packageAddress}, Status: {packageStat}")
        
loadPackages(CSVPackage, packageHashMap)


