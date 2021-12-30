from classes.ninja import Ninja
from classes.pet import Pet


stellas_food = ['Nuti-Source, Dinner Dust']
stellas_treat = ['Greenies, Bully Stick']

stella = Pet('Stella', 'Dog', 'Speak', 'Bark')
paige = Ninja('Paige', 'Milosevic', stella, 'Dinner Dust', 'NutriSource')


print(paige.pet.health)
print(paige.pet.energy)
paige.bathe()
paige.feed()
paige.walk()
print(paige.pet.health)
print(paige.pet.energy)
