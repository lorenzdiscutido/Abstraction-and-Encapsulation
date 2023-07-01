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
    #getters and setters for the private data fields

