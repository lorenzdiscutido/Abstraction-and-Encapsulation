#Import the class fromt the other file
from Pet import Pets
#make a new class
class pet_infos:
    def get_info(self):
        pet = Pets("", "", 0)
#prompt the user to enter name, type, and age
        pet.set_name()
        pet.set_animal_type()
        pet.set_age()
#Display the name, type, and age
        print("")
        print("Your pet infos:")
        pet.get_name()
        pet.get_animal_type()
        pet.get_age()
        print("")

pet = pet_infos()
pet.get_info()