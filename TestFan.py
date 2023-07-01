from The_fan_class import Fan

class TestFan:
    def __init__(self):
        self.fan1 = Fan(Fan.fast, 10, "Yellow", True)
        self.fan2 = Fan(Fan.medium, 5, "Blue", False)

    def show(self):
        print("")
        print("Fan 1")
        print("Speed:", self.fan1.get_speed())
        print("Radius:", self.fan1.get_radius())
        print("Color:", self.fan1.get_color())
        print("On:", self.fan1.get_power())

        print("")
        print("Fan 2")
        print("Speed:", self.fan2.get_speed())
        print("Radius:", self.fan2.get_radius())
        print("Color:", self.fan2.get_color())
        print("On:", self.fan2.get_power())
        print("")
test_run = TestFan()
test_run.show()