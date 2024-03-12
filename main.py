#Student ID: 010604128
from truck import *
from deliveryProcess import*
from helpers import timeValidation
from package import *

truck1 = trucksHashMap.lookup(1)
truck2 = trucksHashMap.lookup(2)
truck3= trucksHashMap.lookup(3)

# print("Truck 1 Departure Time:", truck1.departTime)
# print("Truck 2 Departure Time:", truck2.departTime)
# print("Truck 3 Departure Time:", truck3.departTime)
# print()
# print("Truck 1 Total Miles:", truck1.miles)
# print("Truck 2 Total Miles:", truck2.miles)
# print("Truck 3 Total Miles:", truck3.miles)

# totalMiles = truck1.miles + truck2.miles + truck3.miles
packageHashMap = HashMap()
class Main:
    
    print("Welcome to WGPUS:")
    #print("Total mileage today: ", totalMiles)

    while True:
        time = input("Please enter enquiry time in the format HH:MM:SS or 'q' to quit: ")
        if time.lower() == 'q':
            exit()
            #confirms if time input is proper (found in helpers.py)
        if timeValidation(time):
            loadPackages(CSVPackage, packageHashMap)
            inputTime = timeValidation(time)
            isUpdateTime(inputTime, packageHashMap)
            dispatchTruck(trucksHashMap, inputTime, packageHashMap)
            truck1 = trucksHashMap.lookup(1)
            truck2 = trucksHashMap.lookup(2)
            truck3= trucksHashMap.lookup(3)

            break
        else: 
            print("Invalid format. Please enter a time in the format: HH:MM:SS ")

    #allows for options to be available until user quits
    while True:
        print()
        print("-----------------------------------------------------------------")
        print("S- To find see the status of a package.")
        print("A- To see all package statuses at this time.")
        print("D- to see delivered packages at this time.")
        print("E- to see packages en route at this time.")
        print("H- to see packages at the Hub at this time.")
        print("T- total miles traveled for the whole day.")
        print("Q- Quit")
        userInput = input("What can I help you find? (Type 'q' to quit): ")
        print("-----------------------------------------------------------------")
        print()

        if userInput.lower() == 'q':
            break
        

        #all options except for new time input
        if userInput.lower() in['s', 'a', 'd', 'e',  'h', 't']:
            try:
                #inputTime = timeValidation(time)


                if userInput.lower() == 't':
                    endOfDay = datetime.timedelta(hours=23, minutes=59, seconds=59)
                    for items in packageHashMap.items():
                        packageHashMap.delete(items)
                    loadPackages(CSVPackage, packageHashMap)
                    isUpdateTime(endOfDay, packageHashMap)
                    dispatchTruck(trucksHashMap, endOfDay, packageHashMap) 
                    truck1 = trucksHashMap.lookup(1)
                    truck2 = trucksHashMap.lookup(2)
                    truck3= trucksHashMap.lookup(3)
                    totalMiles = truck1.miles + truck2.miles + truck3.miles
                    print("Total miles traveled for the day: ", totalMiles)


                print("Truck 1 Miles at this time:", truck1.miles)
                print("Truck 2 Miles at this time:", truck2.miles)
                print("Truck 3 Miles at this time:", truck3.miles)
                totalMiles = truck1.miles + truck2.miles + truck3.miles
                print("Total miles traveled at this time: ", totalMiles)

                if userInput.lower() == 's':
                    print("Input time: ", inputTime)
                    singlePackage = input("Enter the package ID: ")   
                    #gets and prints package info for selected package ID 
                    package = packageHashMap.lookup(int(singlePackage))
                    print(package)

                elif userInput.lower() == 'a':
                    print("Input time: ", inputTime)
                    #printing all package info & updating delivery status depending on time
                    for packageID in range(1, 41):
                        package = packageHashMap.lookup(packageID)
                        #status update defined in package.py
                        package.statusUpdate(inputTime)
                        print(package)
                elif userInput.lower() == 'd':
                    print("Input time: ", inputTime)
                    #only prints packages with "Delivered" status at current time
                    packageDelivered = False
                    for packageID in range(1, 41):
                        package = packageHashMap.lookup(packageID)
                        package.statusUpdate(inputTime)
                        if package.status == "Delivered":
                            packageDelivered = True
                            print(package)
                    if not packageDelivered:
                        print("No packages have been delivered at this time.")
                elif userInput.lower() == 'e':
                    print("Input time: ", inputTime)
                        #only prints packages with status of "en route" at input time
                    packagesEnRoute = False
                    for packageID in range(1, 41):
                        package = packageHashMap.lookup(packageID)
                        package.statusUpdate(inputTime)
                        if package.status == "En route":
                            packagesEnRoute = True
                            print(package)
                    if not packagesEnRoute:
                        print("No packages are en route at this time.")
                elif userInput.lower() == 'h':
                    print("Input time: ", inputTime)
                    #only prints packages that have not been delivered or left the hub yet (at current time)
                    packageAtHub = False
                    for packageID in range(1, 41):
                        package = packageHashMap.lookup(packageID)
                        package.statusUpdate(inputTime)
                        if package.status == "At hub":
                            packageAtHub = True
                            print(package)
                    if not packageAtHub:
                        print("No packages are at the Hub at this time.")
                # else:
                #     print("Invalid option. Please try again or type 'q' to quit.")
                #     #if input is not expected value
            except ValueError:
                print("Invalid option. Please try again or type 'q' to quit.")
        else:
            print("Invalid option. Please try again or type 'q' to quit.")
            


