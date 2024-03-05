from readCSV import CSVLocations, CSVDist

def createLocationIndex(locations):
    return {location[2]: index for index, location in enumerate(locations)}

locationIndex = createLocationIndex(CSVLocations)

def getLocationIndex(addressInfo):
    # Convert the address (just street names)
    address = getLocation(addressInfo)

    # Check if the addresse is present in the locationIndex dictionary
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