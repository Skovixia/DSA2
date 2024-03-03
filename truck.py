import datetime
# from helpers import distances
# from helpers import getAddress
# from helpers import packageHashMap
class Truck:
    def __init__(self, maxPackages, speed, load, packages, miles, address, depart):
        self.maxPackages = maxPackages
        self.speed= speed
        self.laod = load
        self.packages = packages
        self.miles = miles
        self.address = address
        self.departTime = depart
        self.time = depart

    def __str__(self):
        return f"{self.maxPackages}, {self.speed}, {self.laod}, {self.packages}, {self.miles}, {self.address}, {self.departTime})"    
    
# Create truck object truck1
truck1 = Truck(16, 18, None,[1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8))

# Create truck object truck2
truck2 = Truck(16, 18,  None, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

# Create truck object truck3
truck3 = Truck(16, 18,  None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=9, minutes=5))

