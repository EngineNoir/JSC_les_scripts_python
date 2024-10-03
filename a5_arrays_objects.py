
# While loops kunnen ook andersom uitgevoerd worden,
# dus i.p.v. i += 1, mag je ook i -= 1
i = 100
while i > 0:
    print(i)
    i -= 1

# arrays en index waardes
A = [2, 3, 5, 7, 11, 13, 17]

print(A[3])
print(A[0])

# array methodes
print(f"Lengte A: {len(A)}")
print(f"Som van A: {sum(A)}")

last = A.pop()
# pop haalt de laatste waarde van een array eruit
# en returnt het
print(last)
# de array zal nu wat kleiner zijn
print(A)
# in python is .append hetzelfde push()
A.append(1)
print(A)
# in python kunnen arrays ook een mix van datatypes bevatten
A.append("nog een priem getal") # zoals een string naast int's
print(A)

# arrays kunnen ook arrays bevatten
B = [[1, 2], ["a", "b"], ["ik", "jij"]]
print(B)
# de eerste element van B is dan dus ook een array, namelijk
# [1, 2]
print(B[0])

# om de eerste elements van elke innerlijke array te printen
output = "" # start met een lege string
for element in B:
    output += str(element[0]) + " " # voeg (als string) de
    # 0de index waarde van elke element (innerlijke array)
print(output)

# klassen

class Character:
    # in python is een __init__() functie nodig om
    # klasses aan te maken
    # self verwijst dus altijd naar het
    # object die geinstantieerd wordt
    def __init__(self, name: str, damage: int, health: int):
        self.name = name
        self.damage = damage
        self.health = health

    # we maken een functie die een target aanvalt
    # en in de functie zie je dat de target.health
    # omlaag gehaald wordt elke keer als attack()
    # gebruikt wordt
    def attack(self, target):
        target.health -= self.damage
        print(f"{self.name} deals {self.damage} damage to {target.name}!")

    # health_check() print de overgebleven health waarde
    def health_check(self):
        print(f"{self.name} has {self.health} health left.")

    # die() checkt of je al overleden bent
    def die(self):
        if self.health <= 0:
            print(f"{self.name} is dead *skull emoji*")


# Enemy is een subklasse van Character
class Enemy(Character):
    def __init__(self, name: str, damage: int, health: int):
        # met super().__init__() maak ik dus een object aan
        # die alle eigenschappen en functies/methodes
        # van de Character superklasse erft
        super().__init__(name, damage, health)

    # taunt is een methode die alleen de subklasse Enemy
    # kan uitvoeren
    def taunt(self, target):
        print(f"{self.name} laughs at {target.name}")

# we initialiseren 2 objects
# de eerste is hero, een object van de klasse Character
# de tweede is villain, een object van de klasse Enemy
hero = Character("Bob", 5, 10)
villain = Enemy("Vampire", 4, 5)

# klein toneel stukje met klasses en objecten
print("\nEPIC FIGHT")
print("----------")
# de villain voert attack() uit met de argument 'hero'
# dus de target parameter wordt nu een object van de
# Character klasse
villain.attack(hero)
# hero checkt zijn overgebleven levens
hero.health_check()
# hero valt de villain aan
hero.attack(villain)
# de villain checkt of hij dood is
villain.die()
# vervolgens voert de villain een speciale method van
# de klasse Enemy uit, namelijk taunt() met als argument
# 'hero'
villain.taunt(hero)
# villain valt hero nog 2 keer aan
villain.attack(hero)
villain.attack(hero)
# de hero overlijdt, helaas is hij geen vampier :(
hero.die()
print("----------")
# met meer uitgebreide logica kunnen dit de basis
# klassen en functies zijn van een spel.
# je zou ook ervoor kunnen zorgen dat attack()
# alleen iets doet als self.health > 0 is.
