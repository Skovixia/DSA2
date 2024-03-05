import datetime
from truck import truck1, truck2, truck3
from package import packageHashMap
from helpers import getLocation, getLocationIndex, distances

def findNextPackage(currentLocation, undeliveredPackages):
    #print("find nearest package starts:")
    currentIndex = getLocationIndex(currentLocation)
    nextAddress = float('inf')
    nextPackage = None

    for package in undeliveredPackages:
        #getting index of every package for distance getter
        packageIndex = getLocationIndex(package.address)
        #for error handling
        if currentIndex is not None and packageIndex is not None:
            #calling function to find distance
            distance = distances(currentIndex,packageIndex)
            #storing smallest distance until a smaller one is found
            if distance <= nextAddress:
                nextAddress = distance
                nextPackage = package

    #print("Found nearest! ", nextAddress)
    return nextPackage

counter = 0
def deliverPackage(truck, packageHashMap):
    global counter
    notDelivered = [packageHashMap.get(packageID) for packageID in truck.packages]
    while notDelivered  and len(truck.packages) <= truck.maxPackages:
        # dynamically gets current location based on the truck's progress
        currentLocation = getLocation(truck.address)
        currentIndex = getLocationIndex(currentLocation)


        # print("Delivery truck ", truck.id)
        # print("-----------------------")
        # print("Truck location: ", truck.address)


        #serachinbg for next closest package
        nextPackage = findNextPackage(currentLocation, notDelivered)
        #sets which truck the package object is assigned to 
        nextPackage.truck = truck.id

        if nextPackage is not None:
            #finding valid location from locations csv
            currentIndex = getLocationIndex(truck.address)
            packageIndex = getLocationIndex(nextPackage.address)

            #print("Next Package address: ", nextPackage.address)

            if currentIndex is not None and packageIndex is not None:

                #getting distance
                distance = distances(currentIndex, packageIndex)
                #print("Distance: ", distance)
                #for me to output total amount of packages delivered
                counter += 1
                #print("Total Packages Delivered: ", counter)
                #error handling for testing
                if distance is not None and distance != float('inf'):

                     # removes the current package from notDelivered
                    notDelivered = [package for package in notDelivered if package.packageID != nextPackage.packageID]
                   
                    # updates truck's mileage
                    truck.miles += distance

                    # updates truck's address after delivering the package
                    truck.address = nextPackage.address
                    #gets total time it took to complete delivery (divide by 1; avg truck speed)
                    deliveryDuration = datetime.timedelta(hours = distance /18)
                    #updating truck time
                    truck.time +=  deliveryDuration
                    #updating departure time and delivery time of current/next package
                    nextPackage.departureTime = truck.departTime
                    nextPackage.deliveryTime = truck.time
                else:
                    print("Error: Invalid distances")
                    break
            else:
                print("Error: Invalid location indices")
                break
        else:
            print("Error: No next package found")
            break

   

deliverPackage(truck1, packageHashMap)
deliverPackage(truck2, packageHashMap)
#sets truck 3 time and depart time to whichever truck finishes deliveries first
truck3.time = min(truck1.time, truck2.time)
truck3.departTime = min(truck1.time, truck2.time)
deliverPackage(truck3, packageHashMap)


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