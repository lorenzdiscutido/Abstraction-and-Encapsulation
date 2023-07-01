from The_fan_class import Fan

class TestFan:
    def test(self):
        fan1 = Fan()
        fan2 = Fan()

        #Set speed
        fan1.set_speed(Fan.fast)
        fan2.set_speed(Fan.medium)
        #Set radius
        fan1.set_radius(10)
        fan2.set_radius(5)
        #Set color
        fan1.set_color("Yellow")
        fan2.get_color()
        #Set power
        fan1.set_power(False)
        fan2.set_power(True)