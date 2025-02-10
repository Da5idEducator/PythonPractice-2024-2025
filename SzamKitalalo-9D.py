# A program generál egy véletlen számot,
# amit a felhasználó megpróbál kitalálni.
# Ha a tippelt szám nagyobb, vagy kisebb,
# mint a generált szám, a program jelzi.

import random

my_file = open("BigBrain.txt", "r")
BigBrain = my_file.read()
# print(BigBrain)

Szam = random.randint(1, 100)
probalkozasok = 0
tippek = []
print(Szam)

tipp = -999
print("Gondoltam egy számra 1 és 100 között.")
print("Próbáld meg kitalálni!")

while tipp != Szam:
    tipp = int(input("Melyik számra gondolhattam?: "))
    probalkozasok = probalkozasok + 1
    tippek.append(tipp)
    
    if tipp > Szam:
        print("Ennél kisebb számra gondoltam.")
        print("Eddigi tippek: ", tippek)
    elif tipp < Szam:
        print("Ennél nagyobb számra gondoltam.")
        print("Eddigi tippek:", tippek)
        
print("*******************************")
print("*                             *")
print("*   G R A T U L Á L O K !     *") 
print("*                             *")
print("*    Ügyesen kitaláltad!      *")
print("*                             *")
print("*******************************")

if probalkozasok < 6:
    print(BigBrain)