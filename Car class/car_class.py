#Make a class
class Car:
#create a constructor for its attributes
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
#function for year model
    def year_model(self):
        return self.__year_model
#Function for make
    def make(self):
        return self.__make
#function for speed