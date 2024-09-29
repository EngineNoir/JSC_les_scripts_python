# LES A4 - LOGICA

# a wordt door ons bepaald. int(..) zet de input om 
# van een string naar een integer
a = int(input("Kies een getal: "))

# hier krijgen wij een ALS ... ANDERS ... blok
# als we voor a 5 kiezen dan print dit "true"
if a == 5:
    print("true")
else:
    print("false")

# dit laat zien dat "a == 5" een BOOLEAN datatype heeft
# oftewel, uitspraken zoals "3 < 5", "True == True", etc 
# zijn zelf BOOLEANS
print(a == 5)

# variabelen kunnen ook BOOLEAN waardes aannemen
p = True
q = True

# de AND evalueert alleen als True als beide inputs
# ook True zijn 
if p and q:
    print("true AND")
else:
    print("not so true AND")

p2 = True
q2 = False

# de OR evalueert True als minstens 1 input
# True is 
# Niet te verwarren met de nederlandse "of" waarbij
# thee of koffie een exclusieve keuze maakt
# OR is meer vergelijkbaar met "en/of"
# "Wil je eten en/of drinken?"
if p or q:
    print("true OR")
else:
    print("not true OR")

# in sommige talen (zoals Python)
# is de ANDERS ... vertakking niet altijd nodig
# als "a > 6" False is, dan gaat de code 
# verder en negeert het de print(...) instructie
if a > 6:
    print("ok")

# de NOT keert een BOOLEAN om, dus 
# not False == True
# not True == False 
if not False:
    print("not false is true")

# while voert iets uit zolang de conditie
# waar is, dus
# TERWIJL (CONDITIE) DOE ...
# in dit geval blijf ik i^2 optellen bij 
# de som totdat i gelijk is aan n 
def optellen_kwadraten(n):
    i = 1
    sum = 0
    while i <= n:
        sum += i*i
        i += 1
    return sum

print(optellen_kwadraten(2))
print(optellen_kwadraten(100))

# de FOR loop doet iets voor elke waarde van een 
# datastructuur, dus in dit geval voor elke stad 
# in mijn array steden print het uit 
# "Ik ben geweest in {stad}"
steden = ["Kaunas", "Londen", "Amsterdam"]
for stad in steden:
    print(f"Ik ben geweest in {stad}")

# deze loop berekent een gemiddelde waarden van 
# een deck kaarten
# voor elke symbol in ["Klaven", "Schoppen", 
# "Harten", "Diamanten"] voeren wij nog een kleine
# loop die telt van 1 t/m 13 (as is 1, boer is 11, 
# dame is 12, en heer is 13)
# (range(a, b) = [a, a+1, ..., b-1], dus 
# range(1, 14) = [1, 2, 3, ..., 11, 12, 13])
# en de cijfer optelt bij de som 
som = 0
for symbol in ["K", "S", "H", "D"]:
    for i in range(1, 14):
        som += i
# vervolgens printen wij de resteerende som/52
# (52 is de totale aantal kaarten, namelijk 4 * 13)
print(som/52)
