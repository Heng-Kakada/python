# # main
#
# from test import Car
#
# car1 = Car("camary", "Red", "Toyota", "2022")
# car2 = Car("highlander", "Silver", "Toyota", "2021")
#
# car1.wheel = 4
#
# print(car1.wheel)
# print(car2.wheel)

class Car:

    wheel = 2  # class variable

    def __init__(self, make, color, brand, year):
        self.make = make  # instance variable
        self.color = color  # instance variable
        self.brand = brand  # instance variable
        self.year = year  # instance variable
