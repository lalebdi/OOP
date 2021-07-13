# "__XX" Will render the object private

class Cars:
    def __init__(self, speed, color):
        self.__speed = speed # made it private
        self.__color = color

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed


ford = Cars(200, "Blue")
nissan = Cars(250, "Red")
toyota = Cars(120, "Silver")


print(ford.get_speed())
ford.set_speed(180)
print(ford.get_speed())

ford.speed = 150
print(ford.get_speed())

