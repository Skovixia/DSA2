from hashmap import HashMap
from readCSV import ReadCSV
# from package import loadPackage 
import datetime
# from package import loadPackage 
from truck import truck1, truck2, truck3
from package import Package


packageHashMap = HashMap()
distCSVFile ="Data\distance.csv"
packageCSVFile = "Data/packages.csv"
addressCSVFile = "Data/address.csv"

csvReadDist = ReadCSV(distCSVFile)
csvReadPackage = ReadCSV(packageCSVFile)
csvReadAddress = ReadCSV(addressCSVFile)

CSVDist = csvReadDist.readCSV()
CSVPackage = csvReadPackage.readCSV()
CSVAddress = csvReadAddress.readCSV()


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
        packageObj = Package(packageID, packageAddress, packageCity, packageState, packageZip, packageDeadLine, packageWeight, packageStat)
        packageHashMap.add(packageID, packageObj)
    


def getAddress(address):
    for row in CSVAddress:
        if address in row[2]:
            return int(row[0])
    return None
        
def distances(x, y):
    distance = CSVDist[x][y]
    if distance =='':
        distance = CSVDist[y][x]
    return float(distance)

loadPackage(CSVPackage, packageHashMap)


def deliverPackage(truck, packageHashMap):
    notDelivered=[]
    for packageID in truck.packages:
        package = packageHashMap.get(packageID)
        if package is None:
            print(f"Package with ID {packageID} not found in packageHashMap.")
            continue  # Skip this package

        notDelivered.append(package)
    truck.packages.clear()

    while len(notDelivered)>0:
        nextAddress = float('inf')
        nextPackage = None
        for package in notDelivered:
            distance = distances(getAddress(truck.address), getAddress(package.address))
            if distance <= nextAddress:
                nextAddress = distance
                nextPackage = package
        if nextPackage is not None:
            truck.packages.append(nextPackage.packageID)
            notDelivered.remove(nextPackage)
            truck.miles += nextAddress
            truck.address = nextPackage.address
            truck.time += datetime.timedelta(hours = nextAddress /18)
            nextPackage.deliveryTime = truck.time
            nextPackage.departureTime = truck.depart
        else:
            break

# packageHashMap = HashMap()
# loadPackage(CSVPackage, packageHashMap)

# print("Contents of packageHashMap before delivery:")
# packageHashMap.printHash()

deliverPackage(truck1, packageHashMap)
deliverPackage(truck2, packageHashMap)
truck3.depart = min(truck1.time, truck2.time)
deliverPackage(truck3, packageHashMap)


# for row in CSVDist:
#     print(row)
# print("Truck 1 Packages:", truck1.packages)
# print("Truck 2 Packages:", truck2.packages)
# print("Truck 3 Packages:", truck3.packages)