import datetime
# from helpers import distances
# from helpers import getAddress
# from helpers import packageHashMap
class Truck:
    def __init__(self, maxPackages, speed, load, packages, miles, address, depart):
        self.maxPackages = maxPackages
        self.speed= speed
        self.load = load
        self.packages = packages
        self.miles = miles
        self.address = address
        self.departTime = depart
        self.time = depart

    def __str__(self):
        return f"{self.maxPackages}, {self.speed}, {self.load}, {self.packages}, {self.miles}, {self.address}, {self.departTime})"    
    
# Create truck object truck1
truck1 = Truck(maxPackages=16, speed=18, load=None, packages=[1, 13, 14, 15, 16, 19, 29, 20, 31, 34, 37, 40],
               miles=0.0, address="4001 South 700 East", depart=datetime.timedelta(hours=8))

# Create truck object truck2
truck2 = Truck(maxPackages=16, speed=18, load=None, packages=[3, 6, 12, 17, 18, 30, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39],
               miles=0.0, address="4001 South 700 East", depart=datetime.timedelta(hours=10, minutes=20))

# Create truck object truck3
truck3 = Truck(maxPackages=16, speed=18, load=None, packages=[2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33],
               miles=0.0, address="4001 South 700 East", depart=datetime.timedelta(hours=9, minutes=5))