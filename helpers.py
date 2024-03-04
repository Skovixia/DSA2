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
from datetime import datetime

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
        packageID, packageAddress, packageCity, packageState, packageZip, packageDeadLine, packageWeight = package[:7]
        # Convert packageID and packageWeight to integers
        packageID = int(packageID)
        packageWeight = int(packageWeight)

        # Parse the time string into a datetime object and then extract minutes
        try:
            packageDeadLine = datetime.strptime(packageDeadLine, '%I:%M %p').time()
            packageDeadLine_minutes = packageDeadLine.hour * 60 + packageDeadLine.minute
        except ValueError:
            packageDeadLine_minutes = None

        packageStat = "At Hub"
        packageObj = Package(packageID, packageAddress, packageCity, packageState, packageZip, packageDeadLine_minutes, packageWeight, packageStat)
        packageInfo.add(packageID, packageObj)

def createLocationIndex(locations):
    return {location[2]: index for index, location in enumerate(locations)}

locationIndex = createLocationIndex(CSVLocations)

# def getLocationIndex(address_info):
#     # Check if the address is present in the locationIndex dictionary
#     if address_info in locationIndex:
#         return locationIndex[address_info]
#     else:
#         # Handle the case when the address is not found
#         print(f"Error: Address '{address_info}' not found in locationIndex.")
#         return None

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
            return row[2]  # Return the full tuple for the address
    return None

import csv

# Replace these paths with your actual file paths
# locations_file_path = "Data/locations.csv"
# distances_file_path = "Data/distance.csv"

# # Read locations from the locations CSV file
# with open(locations_file_path, 'r') as locations_file:
#     locations_reader = csv.reader(locations_file)
#     locations = [row[2] for row in locations_reader]  # Assuming the location is in the third column

# # Read distances from the distances CSV file
# with open(distances_file_path, 'r', encoding='utf-8-sig') as distances_file:  # Add 'encoding' parameter to handle BOM
#     distances_reader = csv.reader(distances_file)
#     # Skip the first row if it contains the BOM marker
#     if distances_file.read(1) == '\ufeff':
#         next(distances_reader)
#     distances_matrix = [[float(value) if value and value != 'inf' else float('inf') for value in row] for row in distances_reader]

# # Number of locations
# num_locations = len(locations)

# # Initialize an empty adjacency matrix with zeros
# adjacency_matrix = [[0.0] * num_locations for _ in range(num_locations)]

# # Fill the adjacency matrix with distances
# for i in range(num_locations):
#     for j in range(num_locations):
#         adjacency_matrix[i][j] = distances_matrix[i][j]

# Print the adjacency matrix
# for row in adjacency_matrix:
#     print(row)


# def createDistanceMatrix(distances):
#     matrix = []
#     for row in distances:
#         row_values = []
#         for value in row:
#             if value == '':
#                 row_values.append(float('inf'))
#             else:
#                 row_values.append(float(value))
#         matrix.append(row_values)
#     return matrix


# print("Location Index:")
# for key, value in locationIndex.items():
#     print(f"{key}: {value}")

# print(locationIndex[1,2])

# distanceMatrix = adjacency_matrix

# def get_distance(location1, location2):
#     index1 = getLocationIndex(location1)
#     index2 = getLocationIndex(location2)

#     if index1 is not None and index2 is not None:
#         return distanceMatrix[index1][index2]
#     else:
#         print(f"Error: One or both locations not found in the index.")
#         return None

# print(distanceMatrix)

def distances(x, y):
    distance = CSVDist[x][y]
    if distance =='':
        distance = CSVDist[y][x]
    return float(distance)

# distanceMatrix = adjacency_matrix

# def printMatrix(matrix):
#     for row in matrix:
#         print(row)

# def distances(x, y):
#     # Check if both indices are valid
#     if x is not None and y is not None:
#         return distanceMatrix[x][y]
#     else:
#         # Handle the case when one or both indices are None
#         print(f"Error: Invalid location indices")
#         return None
    

def find_nearest_package(current_location, undelivered_packages):
    print("find nearest package starts:")

    current_location_index = getLocationIndex(current_location)
    print("Nearest next package cuurent index: ", current_location_index)

    next_address = float('inf')
    next_package = None

    for package in undelivered_packages:
        package_index = getLocationIndex(package.address)
        print("Nearest package index: ", package_index)

        if current_location_index is not None and package_index is not None:
            distance = distances(current_location_index,package_index)
            
            print("Distance of nearest package: ", distance)
            if distance <= next_address and distance:
                next_address = distance
                next_package = package
                print("Nearest next package: ", next_package)
    print("Found nearest! ")
    return next_package


def deliverPackage(truck, packageHashMap):
    notDelivered = [packageHashMap.get(packageID) for packageID in truck.packages]
    
    while notDelivered and len(truck.packages) < truck.maxPackages:
        # Dynamically obtain the current location based on the truck's progress or GPS data
        print("Truck Address: ",truck.address)
        current_location_info = getLocation(truck.address)
        print("Current location: ",current_location_info)
        current_location_index = getLocationIndex(current_location_info)
        print("Current location index: ",current_location_index)

        nextPackage = find_nearest_package(current_location_info, notDelivered)
        print("Next package: ",nextPackage)

        if nextPackage is not None:
            current_location_index = getLocationIndex(truck.address)
            package_location_index = getLocationIndex(nextPackage.address)

            print("Next package address: ",nextPackage.address)
            print(f"Current Location Index: {current_location_index}")
            print(f"Package Location Index: {package_location_index}")

            if current_location_index is not None and package_location_index is not None:
                distance = distances(current_location_index, package_location_index)
                print("Distance: ", distance)
                if distance is not None and distance != float('inf'):
                     # Remove the current package from notDelivered
                    notDelivered = [package for package in notDelivered if package.packageID != nextPackage.packageID]

                    # Update truck's mileage
                    truck.miles += distance

                    # Rest of your code
                    # Update truck's address after delivering the package
                    truck.address = nextPackage.address
                else:
                    print("Error: Invalid distances")
                    break
            else:
                print("Error: Invalid location indices")
                break
        else:
            break

    truck.packages = list(set(truck.packages))
    print(f"Truck {truck.maxPackages} Total Mileage: {truck.miles}")
    print(f"Truck {truck.maxPackages} Packages: {truck.packages}")

# print("Distance Matrix:")
# for row in distanceMatrix:
#     print(row)
#     print("\n")

loadPackage(CSVPackage, packageHashMap)


deliverPackage(truck1, packageHashMap)
deliverPackage(truck2, packageHashMap)
deliverPackage(truck3, packageHashMap)

#print("Location Index:", locationIndex)

# Call the getLocationIndex function
# address = '4001 South 700 East'
# print(f"Address to look up: {address}")
# index = getLocationIndex(address)
# print(f"Location Index Result: {index}")


# print("Location Index:")
# for key, value in locationIndex.items():
#     print(f"{key}: {value}")


# print(distanceMatrix[1])
# deliverPackage(truck2, packageHashMap, distanceMatrix, lo)
# truck3.departTime = min(truck1.time, truck2.time)
# deliverPackage(truck3, packageHashMap, distanceMatrix)


# Print the packages delivered by each truck
# print("Truck 1 Packages:", truck1.packages)
# print("Truck 2 Packages:", truck2.packages)
# print("Truck 3 Packages:", truck3.packages)

# Print matrices
# print("Locations:")
# printMatrix(CSVLocations)
# print("\nDistance Matrix:")
# printMatrix(distanceMatrix)
# print("Location Index:", locationIndex)
