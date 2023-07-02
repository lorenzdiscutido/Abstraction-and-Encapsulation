from car_class import Car
#create a class
    #create the object
car = Car(2004, "Honda")
        
#acceleration of the car(5x)
for i in range(5):
    car.accelerate()
    print("The car's speed is:", car.get_speed())

    #brake of the car(5x)
for i in range(5):
    car.brake()
    print("The car's speed is:", car.get_speed())