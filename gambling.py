import random

kezdopont = 1000
jatekAr = 100
valasz = "i"

roll = []

gyumolcsok = [
    "cseresznye",
    "banán",
    "szilva",
    "7",
    "gyémánt",
    "dinnye",
    "körte",
    "barack",
    "szőlőfürt",
    "csengő"
]

while valasz == "i" or valasz == "I":
    kezdopont = kezdopont - jatekAr
    for i in range (0, 3):
        random.shuffle(gyumolcsok)
        roll.append(gyumolcsok[0])
    
    print(roll)
    print("Bank: ", kezdopont)
    valasz = input("Új játék? I/N: ")
    roll.clear()
    
print("Kifizetés: ", kezdopont)
