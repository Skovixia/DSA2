from hashmap import HashMap
# from readCSV import ReadCSV
# from helpers import deliverPackage
import datetime
# from package import loadPackage 
from truck import truck1, truck2, truck3
from helpers import packageHashMap, loadPackage, CSVPackage, deliverPackage
from package import Package

print("Contents of packageHashMap before delivery:")
packageHashMap.printHash()

print("Truck 1 Packages:", truck1.packages)
print("Truck 2 Packages:", truck2.packages)
print("Truck 3 Packages:", truck3.packages)

print("Truck 1 Packages:", truck1.departTime)
print("Truck 2 Packages:", truck2.departTime)
print("Truck 3 Packages:", truck3.departTime)
totalMiles = truck1.miles + truck2.miles + truck3.miles

class Main:
    print("WGPUS:")
    print("The mileage for the route is: ")
    print(totalMiles)
    

    text = input("To start please type the word 'time' (Anything else will quit the program): ")
    if text == "time":
        try:
            user_time = input("Please enter a time to check the status of a package. Use HH:MM:SS ")
            (h, m, s) = user_time.split(":")
            timeConversion = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            print(timeConversion)
            second_input = input("To view the status of the package please type 'solo' for a rundown of all packages please type 'all': ")
            if second_input == "solo":
                try:
                    solo_input = input("Enter the package ID: ")    
                    package = packageHashMap.get(int(solo_input))
                    print(str(package))
                except ValueError:
                    print("Invalid entry")
                    exit()
            elif second_input == "all":
                try:
                    for packageID in range(1, 41):
                        package = packageHashMap.get(packageID)
                        package.statusUpdate(timeConversion)
                        print(str(package))
                except ValueError:
                    print("Invalid entry")
                    exit()
            else:
                exit()
        except ValueError:
            print("Invalid entry")
            exit()
    elif text != "time":
        print("Invalid entry")
        exit()




