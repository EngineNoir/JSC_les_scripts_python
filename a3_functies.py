# LES A3 - FUNCTIES

# variabel wordt gedeclareerd
x = 20

# functie hoogte met als parameter "tijd"
def hoogte(tijd):
    return 4 * tijd + 2

# print(...) vertoont de waarde die resulteert van het oproepen van hoogte(...)
print(hoogte(5))
print(hoogte(x))

# a is een variabel met een array als waarde
a = [2, 3, 5, 7, 11]

print(f"array: {a}") 
# f"...{a}" formateert de uitkomst op een manier waarop wij a kunnen lezen
print(f"element 1: {a[1]}")
print(f"element 0: {a[0]}")
print(f"laatste element: {a[-1]}") 
# indexen met negatieve waardes levert elementen op vanaf de andere kant (in python!)

# een waarde kan toegevoegd worden aan een array met de .appen() method
a.append(13)

print(f"array na .append: {a}")
print(f"maximal element: {max(a)}") 
# max() is een ingebouwde python functie die de grootste waarde van een datastructuur ophaalt

# hier hebben wij x en y als parameters. Deze x parameter is dus niet verbonden aan de globale x 
# die wij eerder hebben gedefineerd, helemaal aan het begin
def add(x, y):
    return x + y

def add_to_x(y):
    return x + y

def change_a(x):
    a.append(x)

print(add(2,3)) # de uitkomst is 5, zoals verwacht
print(add_to_x(3)) # de uitkomst is 23, hier neemt de functie onze x die bovenaan gedefineerd wordt 
change_a(17) # dit is een functie die 17 toevoegt aan onze array a 
print(a) # hier testen wij of de functie werkelijk a heeft aangepast


