import datetime
from hashmap import HashMap
#from package import packageHashMap
class Truck:
    #class constructor for truck objects
    def __init__(self, truckID, maxPackages, speed, load, packages, miles, address, departureTime):
        self.truckID = truckID
        self.maxPackages = maxPackages
        self.speed= speed
        self.load = load
        self.packages = packages
        self.miles = miles
        self.address = address
        #time will be departure time for delivery function.. allows for time updates
        self.departTime = departureTime
        self.time = departureTime

    def __str__(self):
        return f"{self.maxPackages},{self.truckID}, {self.speed}, {self.load}, {self.packages}, {self.miles}, {self.address}, {self.departTime}"    


#making a hashmap for the truck entities
trucksHashMap = HashMap()
#this function is used to intialize the data for the trunks into the original data for if user enters a new time
#fixes the issue of re-dispatch using previous run's last address and giving different total mileage
def truckInitialize():
            # creating truck objects                                        All packages that have deadline of 10:30 + some EOD packages
    truck1 = Truck(truckID=1, maxPackages=16, speed=18, load=None, packages=[1, 6, 21, 19, 7, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40],
                        miles=0.0, address="4001 South 700 East", departureTime=datetime.timedelta(hours=8))
    trucksHashMap.add(truck1.truckID, truck1)

            #package 9- correct address updates at 10:20, package 25- does not arrive until 9:05, but still arrives before 10:30
    truck2 = Truck(truckID=2, maxPackages=16, speed=18, load=None, packages=[3, 39, 9, 11, 12, 17, 18, 38, 5, 22, 23, 24, 25, 26, 32, 36],
                        miles=0.0, address="4001 South 700 East", departureTime=datetime.timedelta(hours=10, minutes=20))
    trucksHashMap.add(truck2.truckID, truck2)
            #no departure time assignment for truck3, will assign departure time of either truck 1 or 2 depending on when they finish deliveries
    truck3 = Truck(truckID=3, maxPackages=16, speed=18, load=None, packages=[2, 8, 10, 28, 4, 27, 35, 33],
                        miles=0.0, address="4001 South 700 East", departureTime= "TBD")
    trucksHashMap.add(truck3.truckID,truck3)


#function just sets truck ID to packages so when it displays it doesnt say "None"
def truckIDToPackage(truck, packageHashMap):
    #looking up the packages from the packageHashmap of the packages within the truck passed in 
    truckPackages = [packageHashMap.lookup(packageID) for packageID in truck.packages]
    for package in truckPackages:
        package.truck = truck.truckID