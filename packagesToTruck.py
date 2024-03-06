from deliveryProcess import packageHashMap
from helpers import distances, getLocationIndex


#this file helps determime which packages to load into which truck 
eodPackages = []
am10Packages = []
others = []

#loading arrays with appropriate deadlines
for package in packageHashMap.items():
    if package.deadline == "EOD":
        eodPackages.append(package)
    elif package.deadline == "10:30 AM":
        am10Packages.append(package)
    else:
        others.append(package)

#prints packages by deadlines w notes
if eodPackages:
    print("EOD: ")
    print("-----------------------")
    for package in eodPackages:
        print("package Id: ", package.packageID)
        print("Package Deadline: ", package.deadline)
        print("Notes: ", package.notes)
        print("-----------------------")
if am10Packages:
    print("10:30 AM: ")
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


#function prints packges that have the same address
def printPackageAddress(packageHashMap):
    # creating a dictionary to store packageIDs by address
    packagesByAddresses = {}

    # populating the dictionary with packageIDs
    for package in packageHashMap.items():
        address = package.address
        packageID = package.packageID

        if address in packagesByAddresses:
            packagesByAddresses[address].append(packageID)
        else:
            packagesByAddresses[address] = [packageID]


    #prints packages by address
    for address, packageIDs in packagesByAddresses.items():
        print(f"Address: {address}")
        print("Package IDs:", packageIDs)
        print()

        
# items = packageHashMap.items()

# for item in items:
#     print(item)

# print()
#packageHashMap.printHash()
printPackageAddress(packageHashMap)
