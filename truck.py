import datetime
class Truck:
    #class constructor for truck objects
    def __init__(self, id, maxPackages, speed, load, packages, miles, address, departureTime):
        self.id = id
        self.maxPackages = maxPackages
        self.speed= speed
        self.load = load
        self.packages = packages
        self.miles = miles
        self.address = address
        #time will be departure time for delivery function.. allows for time updates
        self.departTime = departureTime
        self.time = departureTime

    def __str__(self):
        return f"{self.maxPackages},{self.id}, {self.speed}, {self.load}, {self.packages}, {self.miles}, {self.address}, {self.departTime})"    

# creating truck objects
truck1 = Truck(id=1, maxPackages=16, speed=18, load=None, packages=[1, 39, 4, 5, 7, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40],
               miles=0.0, address="4001 South 700 East", departureTime=datetime.timedelta(hours=8))

truck2 = Truck(id=2, maxPackages=16, speed=18, load=None, packages=[3, 6, 10, 11, 12, 17, 18, 38, 21, 22, 23, 24, 25, 26, 32, 36],
               miles=0.0, address="4001 South 700 East", departureTime=datetime.timedelta(hours=10, minutes=15))

#no departure time assignment for truck3, will assign departure time of either truck 1 or 2 depending on when they finish deliveries
truck3 = Truck(id=3, maxPackages=16, speed=18, load=None, packages=[2, 8, 9, 28, 19, 27, 35, 33],
               miles=0.0, address="4001 South 700 East", departureTime= datetime.timedelta(hours=0, minutes=0))