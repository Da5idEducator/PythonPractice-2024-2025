# A program megkérdezi a farönk
# átmérőjét és hosszát, majd
# kiszámítja a térfogatát.
# Feltételezzük, hogy a rönkfa
# henger alakú.

beirtAtmero = input("Hány cm. a rönkfa átmérője?: ")
beirtHossz = input("Hány cm. hosszú a rönkfa?: ")

if beirtAtmero.isnumeric() and beirtHossz.isnumeric(): 
    atmero = int(beirtAtmero)
    hossz = int(beirtHossz)
    
    r = atmero / 2
    
    terfogat = (r * r * 3.141) * hossz
    kobmeter = terfogat / 1000000
    
    print("A farönk térfogata", kobmeter, "köbméter.")
    
else:
    print("*** HIBA *** Kérem, egész számokat adjon meg adatként! ***" )