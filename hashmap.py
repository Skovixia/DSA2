import csv

#source citation: Youtube - Python: Creating a HASHMAP using Lists and C950 - Webinar-1 - Let’s Go Hashing - Complete Python Code
class HashMap:
    #constructor with 2 varaibles
    def __init__(self, size=40):
        #set size of array
        self.size = size
        #array to store data in, initiliing every cell to none
        self.map = [None] * self.size
        #self.insertion_order=[]
    
    #private function that takes a key to calculate the index and returns the index
    def _get_hash(self, key):
        return hash(key) % self.size
    
    #takes a key and value
    def add(self, key, value):
        #get the index value we are placing the key in
        key_hash = self._get_hash(key)
        #inserting key value into the cell
        key_value = [key, value]

        #checking if the cell is empty
        if self.map[key_hash] is None or not self.map[key_hash]:
            #adding new list to the index and adding key value to the list
            self.map[key_hash] = [key_value]
            return True
        else:
            for pair in self.map[key_hash]:
                #checking if key already exists
                if pair[0] ==key:
                    #changing value if itr already exists
                    pair[1] = value
                    return True
            #doesnt exist already, appending to the list
            self.map[key_hash].append(key_value)
            #self.insertion_order.append(key_value)
            return True
        
    def lookup(self,key):
        #get the hash using key
        key_hash = self._get_hash(key)
        #locate the cell, checking if it is not None
        if self.map[key_hash] is not None:
            #iterating through pairs in the cell, finding the value matching the key
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    #returning value
                    return pair[1]
        #returning none if not found
        return None
    
    def delete(self, key):
        key_hash = self._get_hash(key)
        #checking if the cell is none, meaning it doesnt exist
        if self.map[key_hash] is None:
            return False
        #need index to remove from the list (using range)
        index = 0
        for item in self.map[key_hash]:
            if item[0] == key:
                self.map[key_hash].pop(index)
                return True
            index +=1
        return False
    
    #function for getting all hashmap items
    def items(self):
        allItems = []
        for cell in self.map:
            if cell is not None:
                for pair in cell:
                    allItems.extend([pair[1] for pair in cell])
                    # allItems.extend(f"({key}, {value})")
        return allItems


    def printHash(self):
        print('---------------------------')
        for key_hash in range(self.size):
            if self.map[key_hash] is not None:
                for key, value in self.map[key_hash]:
                    print(f"Key: {key}, Value: {value}")
        print("End of Hash Map")


#hashmap testing

# h = HashMap()
# h.add("A", 1)
# h.add("B", 2)
# h.add("C", 3)

# h.delete("A")
# h.printHash()
# print("Get: 'C' = ", h.get("C"))


