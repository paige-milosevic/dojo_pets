class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.health += 10
        self.energy += 5
        return self
    
    def play(self):
        self.health += 5
        self.energy -= 15
        return self
    
    def makeNoise(self):
        print(self.noise)

class Ninja:
    def __init__(self, firstName, lastName, pet, treats, petFood):
        self.firstname = firstName
        self.lastname = lastName
        self.pet = pet
        self.treats = treats
        self.petFood = petFood
    
    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        self.pet.eat()
        return self
    
    def bathe(self):
        self.pet.makeNoise()


stella = Pet('Stella', 'Dog', 'Speak', 'Bark')
paige = Ninja('Paige', 'Milosevic', stella, 'Dinner Dust', 'NutriSource')

paige.bathe()

# stella.sleep()
# stella.eat()
# print(stella.health, stella.energy)
# stella.play()
# print(stella.health, stella.energy)