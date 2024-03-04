from hashmap import HashMap
from readCSV import ReadCSV
# from package import loadPackage 
import datetime
# from package import loadPackage 
# from distanceMatrix import adjacency_matrix
from truck import truck1, truck2, truck3
from truck import Truck
from package import Package
import math

packageHashMap = HashMap()
distCSVFile = "Data/distance.csv"
packageCSVFile = "Data/packages.csv"
locationsCSVFile = "Data/locations.csv"

csvReadDist = ReadCSV(distCSVFile)
csvReadPackage = ReadCSV(packageCSVFile)
csvReadLocations = ReadCSV(locationsCSVFile)

CSVDist = csvReadDist.readCSV()
CSVPackage = csvReadPackage.readCSV()
CSVLocations = csvReadLocations.readCSV()

# print(CSVLocations)
# print(CSVDist)

def loadPackage(packageData, packageInfo):
    for package in packageData:
        packageID = int(package[0])
        packageAddress = package[1]
        packageCity = package[2]
        packageState = package[3]
        packageZip = package[4]
        packageDeadLine = package[5]
        packageWeight = package[6]
        packageStat = "At Hub"
        packageTruck = None
        packageDelTime= None
        packageDepartTime = None
        packageObj = Package(packageID, packageAddress, packageCity, packageState, packageZip, packageDeadLine, packageWeight, packageStat, packageTruck, packageDelTime, packageDepartTime)
        packageHashMap.add(packageID, packageObj)
        #print(f"Added package to hashmap - ID: {packageID}, Address: {packageAddress}, Status: {packageStat}")
        
loadPackage(CSVPackage, packageHashMap)

def createLocationIndex(locations):
    return {location[2]: index for index, location in enumerate(locations)}

locationIndex = createLocationIndex(CSVLocations)

def getLocationIndex(address_info):
    # Convert the address_info to a tuple for consistent key format
    address_tuple = getLocation(address_info)
    #print(address_tuple)

    # Check if the address_tuple is present in the locationIndex dictionary
    if address_tuple in locationIndex:
        return locationIndex[address_tuple]
    else:
        # Handle the case when the address is not found
        print(f"Error: Address '{address_info}' not found in locationIndex.")
        return None


def getLocation(address):
    for row in CSVLocations:
        if row[2] == address:
            return row[2]  # Returns the full tuple for the address
    return None


def distances(x, y):
    distance = CSVDist[x][y]
    if distance =='':
        distance = CSVDist[y][x]
    return float(distance)


def find_nearest_package(current_location, undelivered_packages):
    #print("find nearest package starts:")

    current_location_index = getLocationIndex(current_location)
    #print("Nearest next package cuurent index: ", current_location_index)

    next_address = float('inf')
    next_package = None

    for package in undelivered_packages:
        package_index = getLocationIndex(package.address)
        #print("Nearest package index: ", package_index)

        if current_location_index is not None and package_index is not None:
            distance = distances(current_location_index,package_index)
            
            #print("Distance of nearest package: ", distance)
            if distance <= next_address and distance:
                next_address = distance
                next_package = package
                #print("Nearest next package: ", next_package)
    #print("Found nearest! ")
    return next_package


def deliverPackage(truck, packageHashMap):
    notDelivered = [packageHashMap.get(packageID) for packageID in truck.packages]
    
    while notDelivered and len(truck.packages) < truck.maxPackages:
        # Dynamically obtain the current location based on the truck's progress or GPS data
        #print("Truck Address: ",truck.address)
        current_location_info = getLocation(truck.address)
       # print("Current location: ",current_location_info)
        current_location_index = getLocationIndex(current_location_info)
        #print("Current location index: ",current_location_index)

        nextPackage = find_nearest_package(current_location_info, notDelivered)
       # print("Next package: ",nextPackage)
        # nextPackage.truck = truck.id

        if nextPackage is not None:
            current_location_index = getLocationIndex(truck.address)
            package_location_index = getLocationIndex(nextPackage.address)

            # print("Next package address: ",nextPackage.address)
            # print(f"Current Location Index: {current_location_index}")
            # print(f"Package Location Index: {package_location_index}")

            if current_location_index is not None and package_location_index is not None:
                distance = distances(current_location_index, package_location_index)
                #print("Distance: ", distance)
                if distance is not None and distance != float('inf'):
                     # removes the current package from notDelivered
                    notDelivered = [package for package in notDelivered if package.packageID != nextPackage.packageID]

                    # updates truck's mileage
                    truck.miles += distance

                    # updates truck's address after delivering the package
                    truck.address = nextPackage.address
                    truck.time += datetime.timedelta(hours = distance /18)
                    
                    nextPackage.truck = truck.id
                    print("Package truck: ", nextPackage.truck)
                    nextPackage.departureTime = truck.departTime
                    nextPackage.deliveryTime = truck.time
                    
                    
                    print("Truck id: ", truck.id)
                    print("Truck time: ", datetime.timedelta(hours = distance /18) )
                    print("Package depart time: ",nextPackage.departureTime)
                    print("Package delivery time: ",nextPackage.deliveryTime)
                    #print(nextPackage.deadline )
                else:
                    print("Error: Invalid distances")
                    break
            else:
                print("Error: Invalid location indices")
                break
        else:
            break

    truck.packages = list(set(truck.packages))
    print(f"Truck {truck.id} Total Mileage: {truck.miles}")
    print(f"Truck {truck.id} Packages: {truck.packages}")


deliverPackage(truck1, packageHashMap)
# deliverPackage(truck2, packageHashMap)
# truck3.departTime = min(truck1.time, truck2.time)
# deliverPackage(truck3, packageHashMap)

