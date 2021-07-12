def addNumbers(a, b, c=1):
    return a + b + c


print(addNumbers(8, 9))


print(addNumbers(8, 9, 3))


class UK():
    def capital_city(self):
        print("London")

    def language(self):
        print("English")


class Spain():
    def capital_city(self):
        print("Madrid")

    def language(self):
        print("Spanish")


queen = UK()
queen.capital_city()

zara = Spain()
zara.capital_city()

for country in (queen, zara):
    country.capital_city()
    country.language()


def europe(eu):
    eu.capital_city()


europe(zara)