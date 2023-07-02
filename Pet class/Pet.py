#Make a class for pets
class Pets:
    #Make a constructor for the pets
    def __init__(self, name, animal_type,age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    #set name
    def set_name(self):
        name = input("Please input your pet's name:")
        self.__name = name
    #set animal type
    def set_animal_type(self):
        animal_type = input("Please specify your pet's animal type:")
        self.__animal_type = animal_type
    #set age
    def set_age(self):
        age = int(input("Please enter your pet's age:"))
        self.__age = age
    #get name
    def get_name(self):
        print("Name:",self.__name)
        return self.__name
    #get animal type
    def get_animal_type(self):
        print("Animal type:",self.__animal_type)
        return self.__animal_type
    #get age
    def get_age(self):
        print("Age:",self.__age)
        return self.__age