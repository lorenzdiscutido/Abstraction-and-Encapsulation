#Create a class named Fan
class Fan:
    #Declare three constant: slow, medium, and fast
    slow = 1
    medium = 2
    fast = 3
    #Create a constructor for speed, radius, color, and power
    def __init__(self, speed = slow, radius = 5, color = "blue", on=False):
    #Private field for speed of the fan
        self.__speed = speed
    #Private field if the fan is on or off
        self.__power = on
    #Private float field for radius of fan
        self.__radius = radius
    #Private string field for the color of the fan
        self.__color = color
    #getters for the private data fields
    def get_speed(self):
        return self.__speed
    
    def get_power(self):
        return self.__power
    
    def get_radius(self):
        return self.__radius
    
    def get_color(self):
        return self.__color
    #setters for the private data fields
    def set_speed(self, speed):
        self.__speed = speed
    
    def set_power(self, on):
        self.__power = on
    
    def set_radius(self, radius):
        self.__radius = radius
    
    def set_color(self, color):
        self.__color = color


