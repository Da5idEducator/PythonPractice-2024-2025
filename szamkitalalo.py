import random

generaltSzam = random.randint(1, 100)
probalkozasok = 0
beirtSzam = -999

print("Gondoltam egy egész számra, 1 és 100 között.")
print("Próbáld meg kitalálni!")

while True:
    probalkozasok = probalkozasok + 1
    beirtSzam = input("Tipp: ")
    
    if beirtSzam.isnumeric():
        tipp = int(beirtSzam)
        if tipp < generaltSzam:
            print("Ennél nagyobb számra gondoltam.")
        elif tipp > generaltSzam:
            print("Ennél kisebb számra gondoltam.")
        else:
            print("Gratulálok, kitaláltad!")
            print("Próbálkozások száma: ", probalkozasok)
            break
        
    
    
    else:
        print("Ezt nem értem. Kizárólag számot írj be!")
        break