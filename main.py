import datetime
from truck import truck1, truck2, truck3
from helpers import packageHashMap
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
    time = input("Please enter enquiry time or 'q' to quit: ")
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

        if userInput == 'q' or userInput == 'Q':
            break
        
        if userInput in['s', 'S', 'a', 'A', 'd', 'D', 'e', 'E', 'h', 'H']:
            try:
                (h, m, s) = time.split(":")
                timeConversion = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                print("Input time: ", timeConversion)

                if userInput == 's' or userInput == 'S':
                    singlePackage = input("Enter the package ID: ")    
                    package = packageHashMap.get(int(singlePackage))
                    print(package)

                elif userInput == 'a' or userInput == 'A':
                    for packageID in range(1, 41):
                        package = packageHashMap.get(packageID)
                        package.statusUpdate(timeConversion)
                        print(package)
                elif userInput == 'D' or userInput == 'd':
                    packageDelivered = False
                    for packageID in range(1, 41):
                        package = packageHashMap.get(packageID)
                        package.statusUpdate(timeConversion)
                        if package.status == "Delivered":
                            packageDelivered = True
                            print(package)
                        if not packageDelivered:
                            print("No packages have been delivered at this time.")
                elif userInput == 'E' or userInput == 'e':
                        packagesEnRoute = False
                        for packageID in range(1, 41):
                            package = packageHashMap.get(packageID)
                            package.statusUpdate(timeConversion)
                            if package.status == "En route":
                                packagesEnRoute = True
                                print(package)
                        if not packagesEnRoute:
                             print("No packages are en route at this time.")
                elif userInput == 'H' or userInput == 'h':
                    packageAtHub = False
                    for packageID in range(1, 41):
                        package = packageHashMap.get(packageID)
                        package.statusUpdate(timeConversion)
                        if package.status == "At Hub":
                            packageAtHub = True
                            print(package)
                        if not packageAtHub:
                            print("No packages are at the Hub at this time.")
                else:
                    print("Invalid option. Please try again or type 'q' to quit.")
            except ValueError:
                print("Invalid option. Please try again or type 'q' to quit.")
        elif userInput == 't' or userInput == 'T':
            time = input("Please enter enquiry time or 'q' to quit: ")
            try:
                (h, m, s) = time.split(":")
                timeConversion = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                print("Input time: ", timeConversion)
            except ValueError:
                print("Invalid option. Please try again or type 'q' to quit.")



