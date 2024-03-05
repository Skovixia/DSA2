import datetime
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
        if timeValidation(time):
            break
        else: 
            print("Invalid format. Please enter a time in the format: HH:MM:SS ")


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
        
        if userInput in['s', 'S', 'a', 'A', 'd', 'D', 'e', 'E', 'h', 'H']:
            try:

                print("Input time: ", time)

                if userInput.lower() == 's':
                    singlePackage = input("Enter the package ID: ")    
                    package = packageHashMap.get(int(singlePackage))
                    print(package)

                elif userInput.lower() == 'a':
                    for packageID in range(1, 41):
                        package = packageHashMap.get(packageID)
                        package.statusUpdate(timeValidation(time))
                        print(package)
                elif userInput.lower() == 'd':
                    packageDelivered = False
                    for packageID in range(1, 41):
                        package = packageHashMap.get(packageID)
                        package.statusUpdate(timeValidation(time))
                        if package.status == "Delivered":
                            packageDelivered = True
                            print(package)

                    if not packageDelivered:
                        print("No packages have been delivered at this time.")
                elif userInput.lower() == 'e':
                        packagesEnRoute = False
                        for packageID in range(1, 41):
                            package = packageHashMap.get(packageID)
                            package.statusUpdate(timeValidation(time))
                            if package.status == "En route":
                                packagesEnRoute = True
                                print(package)
                        if not packagesEnRoute:
                             print("No packages are en route at this time.")
                elif userInput.lower() == 'h':
                    packageAtHub = False
                    for packageID in range(1, 41):
                        package = packageHashMap.get(packageID)
                        package.statusUpdate(timeValidation(time))
                        if package.status == "At Hub":
                            packageAtHub = True
                            print(package)
                    if not packageAtHub:
                        print("No packages are at the Hub at this time.")
                else:
                    print("Invalid option. Please try again or type 'q' to quit.")
            except ValueError:
                print("Invalid option. Please try again or type 'q' to quit.")
        elif userInput.lower() == 't':
            while True:
                newTime = input("Please enter enquiry time or 'q' to quit: ")
                if newTime.lower()== 'q':
                    break
                if timeValidation(newTime):
                    time = newTime
                    break
                else:
                    print("Invalid format. Please enter a time in the format: HH:MM:SS ")
        else:
            print("Invalid option. Please try again or type 'q' to quit.")
            


