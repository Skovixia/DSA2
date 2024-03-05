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
        #assigning a truck to each package(for debugging)
        self.truck = truck
        #setting del time and depart time to non, will be updated when delivered
        self.deliveryTime= None
        self.departureTime = None
        self.notes = notes
    def __str__(self):
        #for interface.. It not delivered yet, will display "estimated delivery"
        if self.status == "Delivered":
            deliveryLabel = "Delivery Time" 
        else:
            deliveryLabel = "Estimated Delivery Time"

        strLength = len(f"|{self.packageID}| Destination: {self.address}, {self.city}, {self.state}, {self.zip}| Deadline: {self.deadline}| Weight: {self.weight}| Truck: {self.truck}| Departure Time: {self.departureTime}| {deliveryLabel}: {self.deliveryTime}| Status: {self.status}")
        print("-" * strLength)
        return f"|{self.packageID}| Destination: {self.address}, {self.city}, {self.state}, {self.zip}| Deadline: {self.deadline}| Weight: {self.weight}| Truck: {self.truck}| Departure Time: {self.departureTime}| {deliveryLabel}: {self.deliveryTime}| Status: {self.status}"
        
    
    #for updating status based on time given in main
    def statusUpdate(self, enquiryTime):
        if self.deliveryTime < enquiryTime:
            self.status = "Delivered"
        elif self.departureTime <= enquiryTime <= self.deliveryTime:
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



    # def statusUpdate(self, timeConversion):
    #     if self.deliveryTime is not None and timeConversion is not None:
    #         if isinstance(self.deliveryTime, datetime.timedelta) and isinstance(timeConversion, datetime.timedelta):
    #             if self.deliveryTime < timeConversion:
    #                 self.status = "Delivered"
    #             elif self.departureTime > timeConversion: 
    #                 self.status = "En route"
    #             else:
    #                 self.status = "En route"
    #         else:
    #             print("-------------------------------------------")
    #             print("ERROR: Invalid time format for comparison")
    #             print("-------------------------------------------")
    #     else:
    #         print("-------------------------------------------")
    #         print("Error: Delivery time or time conversion is None")
    #         print("-------------------------------------------")
