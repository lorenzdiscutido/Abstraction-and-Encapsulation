from The_fan_class import Fan

class TestFan:
    def __init__(self):
        self.fan1 = Fan(Fan.fast, 10, "Yellow", False)
        self.fan2 = Fan(Fan.medium, 5, "Blue", True)

    def show(self):
        print("Fan 1")
        print("Speed:", self.fan1.get_speed())

test_run = TestFan()
test_run.show()