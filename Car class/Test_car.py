from car_class import Car

car = Car(2004, "Honda")
        
for i in range(5):
    car.accelerate()
    print("The car's speed is:", car.get_speed())

for i in range(5):
    car.brake()
    print("The car's speed is:", car.get_speed())