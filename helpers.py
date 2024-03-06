from readCSV import CSVLocations, CSVDist
import datetime

#This file contains additional getters ie. location index, getting location, distance finder + time format validator for main


#just reads through locations.csv (second col) stores addresses into dictionary
def createLocationDictionary(locations):
    return {location[2]: index for index, location in enumerate(locations)}

#sends locations.csv info to creation dictionary
locationDict = createLocationDictionary(CSVLocations)

#dictionary key is the address, value is the index; this returns the index 
def getLocationIndex(address):
    return locationDict.get(address)


#locates the appropriate distance from distance.csv (read like matrix) using the location indexes(numeric values)
def distances(index1, index2):
    try:
        distance = CSVDist[index1][index2]
        if distance =='':
        #direction doesnt matter
            distance = CSVDist[index2][index1]
        return float(distance)
    except IndexError:
        print("Invalid indexes provided: ", index1, index2)
        return None


#for proper time formatting in interface
def timeValidation(time):
    #splits time into parts
    hms = time.split(":")
    if len(hms) == 3:
        try:
            hours = int(hms[0])
            minutes = int(hms[1])
            seconds = int(hms[2])
            #confirms that time input is within the proper constraints for h, m, s
            if 0 <= hours < 24 and 0<= minutes < 60 and 0<= seconds < 60:
                return datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
        except ValueError:
            #null operation (dpes nothing)
            pass
    return False





### OLD Functions:
# def getLocation(address):
#     for row in CSVLocations:
#         if row[2] == address:
#             #returns just the street address
#             return row[2]  
#     return None

# def getLocationIndex(addressInfo):
#     # converts the address (just street names)
#     address = getLocation(addressInfo)

#     # checks if the addresse is present in the locationIndex dictionary
#     if address in locationDict:
#         #returns index of the address (numeric value)
#         return locationDict[address]
#     else:
#         # handles if address not found
#         print(f"Error: Address '{addressInfo}' not found in locationIndex.")
#         return None


# def getLocationIndex(addressInfo):
#     for address, index in locationDict.items():
#         if getLocation(address) == addressInfo:
#             return address
