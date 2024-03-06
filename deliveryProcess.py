import datetime
from truck import *
from package import packageHashMap
from helpers import *

counter = 0

#sorts the packages in the truck in order by distance
def sortPackages(currentIndex, truck):
    unOrderedPackages = [packageHashMap.lookup(packageID) for packageID in truck.packages]
    sortedPackages = []
    while unOrderedPackages:
        #print("find nearest package starts:")
        shortestDistance = float('inf')
        nextPackage = None

        for package in unOrderedPackages:
        #getting index of every package for distance getter
            packageIndex = getLocationIndex(package.address)
        #for error handling
            if currentIndex is not None and packageIndex is not None:
            #calling function to find distance
                distance = distances(currentIndex,packageIndex)
            #storing smallest distance until a smaller one is found
                if distance <= shortestDistance:
                    shortestDistance = distance
                    nextPackage = package
        if nextPackage:
            #adds current package to sorted list
            sortedPackages.append(nextPackage)
            #removes current package from unordered list to stop from iterating over the same packages
            unOrderedPackages.remove(nextPackage)
            currentIndex = getLocationIndex(nextPackage.address)
        else:
            break

    #print("Found nearest! ", nextAddress)
    return sortedPackages



def deliverPackage(truck, packageHashMap):
    global counter
    #gets current location based on the truck's progress
    sortedPackages = sortPackages(getLocationIndex(truck.address), truck)

    print("Sorted packages: ")
    for package in sortedPackages:
        print(package.packageID)
    
    for package in sortedPackages:
        #sets which truck the package object is assigned to 
        package.truck = truck.id
        #retrieves index from location dictionary in helpers.py
        #print("Next Package: ", package.packageID)
        currentIndex = getLocationIndex(truck.address)
        packageIndex = getLocationIndex(package.address)
        if currentIndex is not None and packageIndex is not None:
            #getting distance
            distance = distances(currentIndex, packageIndex)
            #print("Distance: ", distance)
            counter += 1 #outputs total amount of delivered packages for testing
                
                #error handling for testing
            if distance is not None and distance != float('inf'):
                #gets total time it took to complete delivery (divide by 18; avg truck speed)
                deliveryDuration = datetime.timedelta(hours = distance /18)

                    # updates truck's mileeage, address, time and departure time after delivering the package
                truck.miles += distance
                truck.address = package.address
                truck.time +=  deliveryDuration
                package.departureTime = truck.departTime
                package.deliveryTime = truck.time
            else:
                print("Error: Invalid distances")
                break
        else:
            print("Error: Invalid location indices")
            break
      

#print("COUNTER: ",counter)
   

deliverPackage(truck1, packageHashMap)
deliverPackage(truck2, packageHashMap)
#sets truck 3 time and depart time to whichever truck finishes deliveries first
truck3.time = min(truck1.time, truck2.time)
truck3.departTime = min(truck1.time, truck2.time)
deliverPackage(truck3, packageHashMap)


# deliverPackage(truck1, packageHashMap)
# deliverPackage(truck2, packageHashMap)
# #sets truck 3 time and depart time to whichever truck finishes deliveries first
# truck3.time = min(truck1.time, truck2.time)
# truck3.departTime = min(truck1.time, truck2.time)
# deliverPackage(truck3, packageHashMap)




#Old next package:
# def findNextPackage(currentIndex, undeliveredPackages):
#     #print("find nearest package starts:")
#     nextAddress = float('inf')
#     nextPackage = None

#     for package in undeliveredPackages:
#         #getting index of every package for distance getter
#         packageIndex = getLocationIndex(package.address)
#         #for error handling
#         if currentIndex is not None and packageIndex is not None:
#             #calling function to find distance
#             distance = distances(currentIndex,packageIndex)
#             #storing smallest distance until a smaller one is found
#             if distance <= nextAddress:
#                 nextAddress = distance
#                 nextPackage = package

#     #print("Found nearest! ", nextAddress)
#     return nextPackage




  #error finding
    # print("Delivery truck ", truck.id)
    # print("-----------------------")

#Testing print statements
 # truck.packages = list(set(truck.packages))
    # print(f"Truck {truck.id} Total Mileage: {truck.miles}")
    # print(f"Truck {truck.id} Packages: {truck.packages}")

  
                    # print("Truck id: ", truck.id)
                    # print("Delivery duration: ", deliveryDuration)
                    # print("Truck time: ", truck.time )
                    # print("Package depart time: ",nextPackage.departureTime)
                    # print("Package delivery time: ",nextPackage.deliveryTime)
                    #print(nextPackage.deadline )


# def deliverPackage(truck, packageHashMap):
#     global counter
#     notDelivered = [packageHashMap.lookup(packageID) for packageID in truck.packages]

#     while len(notDelivered) > 0:
#         #gets current location based on the truck's progress
#         currentIndex = getLocationIndex(truck.address)

#         #seraching for next closest package
#         nextPackage = findNextPackage(currentIndex, notDelivered)

#         #sets which truck the package object is assigned to 
#         nextPackage.truck = truck.id

#         if nextPackage is not None:
#             #retrieves index from location dictionary in helpers.py
#             currentIndex = getLocationIndex(truck.address)
#             packageIndex = getLocationIndex(nextPackage.address)

#             if currentIndex is not None and packageIndex is not None:

#                 #getting distance
#                 distance = distances(currentIndex, packageIndex)
                
#                 counter += 1 #outputs total amount of delivered packages for testing
                
#                 #error handling for testing
#                 if distance is not None and distance != float('inf'):
#                     # removes the current package from notDelivered
#                     notDelivered.remove(nextPackage)
                    
#                     #gets total time it took to complete delivery (divide by 18; avg truck speed)
#                     deliveryDuration = datetime.timedelta(hours = distance /18)

#                     # updates truck's mileeage, address, time and departure time after delivering the package
#                     truck.miles += distance
#                     truck.address = nextPackage.address
#                     truck.time +=  deliveryDuration
#                     nextPackage.departureTime = truck.departTime
#                     nextPackage.deliveryTime = truck.time
#                 else:
#                     print("Error: Invalid distances")
#                     break
#             else:
#                 print("Error: Invalid location indices")
#                 break
#         else:
#             print("Error: No next package found")
#             break
