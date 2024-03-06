from readCSV import CSVLocations, CSVDist
import datetime

def createLocationIndex(locations):
    return {location[2]: index for index, location in enumerate(locations)}

locationIndex = createLocationIndex(CSVLocations)

def getLocationIndex(addressInfo):
    # converts the address (just street names)
    address = getLocation(addressInfo)

    # checks if the addresse is present in the locationIndex dictionary
    if address in locationIndex:
        return locationIndex[address]
    else:
        # handles if address not found
        print(f"Error: Address '{addressInfo}' not found in locationIndex.")
        return None


def getLocation(address):
    for row in CSVLocations:
        if row[2] == address:
            #returns just the street address
            return row[2]  
    return None


def distances(index1, index2):
    #locates the appropriate distance from distance.csv (read like matrix)
    distance = CSVDist[index1][index2]
    if distance =='':
        distance = CSVDist[index2][index1]
    return float(distance)


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