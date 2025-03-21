import random

targyak = [
    "cuki plüss cica",
    "szív alakú csokidesszert",
    "egy csokor vörös rózsa",
    "Lego orchidea",
    "Nyaklánc",
    "Kép album",
    "Szájfény",
    "Könyv",
    "Lávalámpa"
]

#print(targyak)
#print(targyak[9])

titok = random.randint(0, len(targyak))
print(titok)
print(targyak[titok])

print("A tárgyak listája:")

for i in targyak:
    print(i)