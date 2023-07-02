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
    def accelerate(self):
        if self.__speed <5:
            self.__speed =+ 5
        else:
            self.__speed = 5
    
    def brake(self):
        if self.__speed>=5:
            self.__speed +- 5
        else:
            self.__speed = 0

    def get_speed(self):
        return self.__speed