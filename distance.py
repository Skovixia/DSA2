from hashmap import HashMap
import csv
class Distance:

    # def __init__(self, stop1, stop2, dist):
    #     self.stop1= stop1
    #     self.stop2= stop2
        
    #     self.dist = dist

    # def getDist(self):
    #     return self.dist
    # def setDist(self, dist):
    #     self.dist = dist
    
    
# addressesHashMap = HashMap()
# with open('Data/address.csv', encoding='utf-8-sig', newline='') as file:
#     reader = csv.reader(file)
#     for row in 
    distances=[]
    distCSVFile ="Data\distance.csv"
    with open(distCSVFile, encoding='utf-8-sig', newline='') as file:
        reader = csv.reader(file)
        # distances = [[dist if dist.strip() else "NA" for dist in row] for row in reader]
   #header = next(reader)
        for row in reader:
            distance_row =[dist if dist.strip() else "NA" for dist in row]
            distances.append(distance_row)

    # for distance_row in distances:
    #     print(distance_row)
    
    addressesHashMap = HashMap()

# Read addresses.csv
    addressCSVFile = "Data/address.csv"
    with open(addressCSVFile, encoding='utf-8-sig', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            index, address, location = row[0],row[1], row[2]
            distances_for_address = distances[int(index)] 
            addressesHashMap.add(address, distances_for_address)
# Printing HashMap
    addressesHashMap.printHash()