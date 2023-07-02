from car_class import Car
#create a class
class TestCar:
    #create the object
    def show(self):
        car = Car(2004, "Honda")
        
        #acceleration of the car(5x)
        for i in range(5):
            car.accelerate()
            print("The car's speed is:", car.get_speed())

        #brake of the car(5x)
        for i in range(5):
            car.brake()
            print("The car's speed is:", car.get_speed())

test_run = TestCar
test_run.show()
