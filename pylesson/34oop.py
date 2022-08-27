class Car:
    # make = None
    # color = None
    # Brand = None
    # year = None

    def __init__(self, make, color, brand, year):
        self.make = make
        self.color = color
        self.brand = brand
        self.year = year

    def drive(self):
        print(f"This {self.make} is driving")

    def stop(self):
        print(f"This {self.make} is stop")

# main

# OOP
# from oop import Car
#
# car1 = Car("Chevy", "Red", "BMW", "2002")
# car2 = Car("camary", "silver", "Toyota", "2022")
#
# print(car1.make)
# print(car1.color)
# print(car1.brand)
# print(car1.year)
#
# print(car2.make)
# print(car2.color)
# print(car2.brand)
# print(car2.year)
#
# car1 .drive()
# car2.stop()
