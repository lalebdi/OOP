# "__XX" Will render the object private

class Cars:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def set_speed(self, value):
        self.speed = value

    def get_speed(self):
        return self.speed


ford = Cars(200, "Blue")
nissan = Cars(250, "Red")
toyota = Cars(120, "Silver")



