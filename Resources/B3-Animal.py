class Animal:
    #animal constructor
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self._age = 0
        self.__curr_spd = 0.0

    def eat(self, food):
        return self.name + " ate " + food

    def change_spd(self, speed):
        self.__curr_spd = speed

    def grow_up(self, years):
        self._age += years

    def getAge(self):
        return self._age

    def getCurrSpd(self):
        return self.__curr_spd

    def setName(self, name):
        self.name = name

    def __str__(self):
        return self.name + " the " + self.species + " is " + str(self._age) + " years old, and is moving at " + str(self.__curr_spd) + " miles per hour."





#main code

#testing constructor
ani = Animal("Wilhelmina", "Corn Snake")

#testing tostring
print(ani)

#testing eat function
print(ani.eat("rat"))

#testing change speed function
ani.change_spd(3.0)
print(ani)

#testing grow up function
ani.grow_up(3)
print(ani)

print(ani.getAge())
print(ani.getCurrSpd())

ani.setName("Aspen")
print(ani)





