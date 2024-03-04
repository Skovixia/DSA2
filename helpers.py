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
        packageAddress, packageCity, packageState, packageZip, packageDeadLine, packageWeight, packageNotes = package[1:8]
        packageStat = "At Hub"
        packageTruck = None
        packageDelTime= None
        packageDepartTime = None
        packageObj = Package(packageID, packageAddress, packageCity, packageState, packageZip, packageDeadLine, packageWeight, packageStat, packageTruck, packageDelTime, packageDepartTime, packageNotes)
        packageHashMap.add(packageID, packageObj)
        #print(f"Added package to hashmap - ID: {packageID}, Address: {packageAddress}, Status: {packageStat}")
        
loadPackage(CSVPackage, packageHashMap)

eodPackages = []
am10Packages = []
others = []

for package in packageHashMap.items():
    if package.deadline == "EOD":
        eodPackages.append(package)
    elif package.deadline == "10:30 AM":
        am10Packages.append(package)
    else:
        others.append(package)


if eodPackages:
    print("EOD: ")
    print("-----------------------")
    for package in eodPackages:
        print("package Id: ", package.packageID)
        print("Package Deadline: ", package.deadline)
        print("Notes: ", package.notes)
        print("-----------------------")
if am10Packages:
    print("10:00 AM: ")
    print("-----------------------")
    for package in am10Packages:
        print("package Id: ", package.packageID)
        print("Package Deadline: ", package.deadline)
        print("Notes: ", package.notes)
        print("-----------------------")
if others:
    print("Others: ")
    print("-----------------------")
    for package in others:
        print("package Id: ", package.packageID)
        print("Package Deadline: ", package.deadline)
        print("Notes: ", package.notes)
        print("-----------------------")



def print_package_ids_by_address(package_hashmap):
    # Create a dictionary to store package IDs by address
    package_ids_by_address = {}

    # Populate the dictionary with package IDs
    for package in package_hashmap.items():
        address = package.address
        package_id = package.packageID

        if address in package_ids_by_address:
            package_ids_by_address[address].append(package_id)
        else:
            package_ids_by_address[address] = [package_id]

    # Print package IDs for each address
    for address, package_ids in package_ids_by_address.items():
        print(f"Address: {address}")
        print("Package IDs:", package_ids)
        print()

print_package_ids_by_address(packageHashMap)



def createLocationIndex(locations):
    return {location[2]: index for index, location in enumerate(locations)}

locationIndex = createLocationIndex(CSVLocations)

def getLocationIndex(addressInfo):
    # Convert the address_info to a tuple for consistent key format
    address = getLocation(addressInfo)
    #print(address_tuple)

    # Check if the address_tuple is present in the locationIndex dictionary
    if address in locationIndex:
        return locationIndex[address]
    else:
        # Handle the case when the address is not found
        print(f"Error: Address '{addressInfo}' not found in locationIndex.")
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

def optomizedDelivery(truck, truckPackages):
    #sorts undelivered packages using distance from trucks current location
    truckPackages.sort(key = lambda package: distances(getLocationIndex(truck.address), getLocationIndex(package.address)))
    return truckPackages

def find_nearest_package(currentLocation, undeliveredPackages):
    #print("find nearest package starts:")

    currentIndex = getLocationIndex(currentLocation)
    #print("Nearest next package cuurent index: ", current_location_index)

    nextAddress = float('inf')
    nextPackage = None

    for package in undeliveredPackages:
        packageIndex = getLocationIndex(package.address)
        #print("Nearest package index: ", package_index)

        if currentIndex is not None and packageIndex is not None:
            distance = distances(currentIndex,packageIndex)
            
            #print("Distance of nearest package: ", distance)
            if distance <= nextAddress:
                nextAddress = distance
                nextPackage = package
                #print("Nearest next package: ", nextPackage)
    #print("Found nearest! ", nextAddress)
    return nextPackage


def deliverPackage(truck, packageHashMap):
    notDelivered = [packageHashMap.get(packageID) for packageID in truck.packages]
    # for package in notDelivered:
    print("Delivery truck ", truck.id)
    print("-----------------------")
    #print(len(truck.packages))
    #print(truck.maxPackages)
    while notDelivered  and len(truck.packages) <= truck.maxPackages:
        # Dynamically obtain the current location based on the truck's progress or GPS data
        #print("Truck Address: ",truck.address)
        currentLocation = getLocation(truck.address)
        currentIndex = getLocationIndex(currentLocation)
        #print("Current location ",currentLocation)

        nextPackage = find_nearest_package(currentLocation, notDelivered)
        #print("Next package: ",nextPackage)
        nextPackage.truck = truck.id

        if nextPackage is not None:
            currentIndex = getLocationIndex(truck.address)
            packageIndex = getLocationIndex(nextPackage.address)


            print("PAckage id: ", nextPackage.packageID)
            print("Next package address: ",nextPackage.address)
            # print(f"Current Location Index: {current_location_index}")
            # print(f"Package Location Index: {package_location_index}")

            if currentIndex is not None and packageIndex is not None:
                distance = distances(currentIndex, packageIndex)
                print("Distance: ", distance)
                if distance is not None and distance != float('inf'):
                     # removes the current package from notDelivered
                    notDelivered = [package for package in notDelivered if package.packageID != nextPackage.packageID]
                    # for package in notDelivered:
                    #     print("Not delivered: ",package)
                    # updates truck's mileage
                    truck.miles += distance

                    # updates truck's address after delivering the package
                    truck.address = nextPackage.address
                    truck.time += datetime.timedelta(hours = distance /18)
                    nextPackage.truck = truck.id
                    #print("Package truck: ", nextPackage.truck)
                    nextPackage.departureTime = truck.departTime
                    nextPackage.deliveryTime = truck.time
                    
                    
                    # print("Truck id: ", truck.id)
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
            print("Error: No next package found")
            break

    truck.packages = list(set(truck.packages))
    print(f"Truck {truck.id} Total Mileage: {truck.miles}")
    # print(f"Truck {truck.id} Packages: {truck.packages}")

# optomizedDelivery(truck1, truck1.packages)
# optomizedDelivery(truck2, truck2.packages)
# optomizedDelivery(truck2, truck2.packages)

deliverPackage(truck1, packageHashMap)
deliverPackage(truck2, packageHashMap)
truck3.departTime = min(truck1.time, truck2.time)
deliverPackage(truck3, packageHashMap)

