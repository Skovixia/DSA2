#Student ID: 010604128
from truck import truck1, truck2, truck3
from deliveryProcess import packageHashMap
from helpers import timeValidation
# print("Truck 1 Packages:", truck1.packages)
# print("Truck 2 Packages:", truck2.packages)
# print("Truck 3 Packages:", truck3.packages)
# print()
print("Truck 1 Departure Time:", truck1.departTime)
print("Truck 2 Departure Time:", truck2.departTime)
print("Truck 3 Departure Time:", truck3.departTime)
totalMiles = truck1.miles + truck2.miles + truck3.miles

class Main:
    
    print("Welcome to WGPUS:")
    print("Total mileage today: ", totalMiles)

    while True:
        time = input("Please enter enquiry time or 'q' to quit: ")
        if time.lower() == 'q':
            exit()
            #confirms if time input is proper (found in helpers.py)
        if timeValidation(time):
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
        print("T- To see options for another time.")
        print("Q- Quit")
        userInput = input("What can I help you find? (Type 'q' to quit): ")
        print("-----------------------------------------------------------------")
        print()

        if userInput.lower() == 'q':
            break
        #all options except for new time input
        if userInput in['s', 'S', 'a', 'A', 'd', 'D', 'e', 'E', 'h', 'H']:
            try:

                print("Input time: ", time)

                if userInput.lower() == 's':
                    singlePackage = input("Enter the package ID: ")   
                    #gets and prints package info for selected package ID 
                    package = packageHashMap.lookup(int(singlePackage))
                    print(package)

                elif userInput.lower() == 'a':
                    #printing all package info & updating delivery status depending on time
                    for packageID in range(1, 41):
                        package = packageHashMap.lookup(packageID)
                        #status update defined in package.py
                        package.statusUpdate(timeValidation(time))
                        print(package)
                elif userInput.lower() == 'd':
                    #only prints packages with "Delivered" status at current time
                    packageDelivered = False
                    for packageID in range(1, 41):
                        package = packageHashMap.lookup(packageID)
                        package.statusUpdate(timeValidation(time))
                        if package.status == "Delivered":
                            packageDelivered = True
                            print(package)
                    if not packageDelivered:
                        print("No packages have been delivered at this time.")
                elif userInput.lower() == 'e':
                        #only prints packages with status of "en route" at input time
                    packagesEnRoute = False
                    for packageID in range(1, 41):
                        package = packageHashMap.lookup(packageID)
                        package.statusUpdate(timeValidation(time))
                        if package.status == "En route":
                            packagesEnRoute = True
                            print(package)
                    if not packagesEnRoute:
                        print("No packages are en route at this time.")
                elif userInput.lower() == 'h':
                    #only prints packages that have not been delivered or left the hub yet (at current time)
                    packageAtHub = False
                    for packageID in range(1, 41):
                        package = packageHashMap.lookup(packageID)
                        package.statusUpdate(timeValidation(time))
                        if package.status == "At hub":
                            packageAtHub = True
                            print(package)
                    if not packageAtHub:
                        print("No packages are at the Hub at this time.")
                else:
                    print("Invalid option. Please try again or type 'q' to quit.")
                    #if input is not expected value
            except ValueError:
                print("Invalid option. Please try again or type 'q' to quit.")
        elif userInput.lower() == 't':
            #option for new time input
            while True:
                newTime = input("Please enter enquiry time or 'q' to quit: ")
                if newTime.lower()== 'q':
                    break
                #validating time
                if timeValidation(newTime):
                    time = newTime
                    break
                else:
                    print("Invalid format. Please enter a time in the format: HH:MM:SS ")
        else:
            print("Invalid option. Please try again or type 'q' to quit.")
            


