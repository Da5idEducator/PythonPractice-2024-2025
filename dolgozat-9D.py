# 1. Kérjen be a program a felhasználótól 
# két egész számot!
a = int(input("Írj be egy egész számot!: "))
b = int(input("Írj be egy egész számot!: "))

# 2. Írja ki a program, hogy melyik 
# szám a nagyobb!
if a > b:
    print("A nagyobb szám: ", a)
elif a < b:
    print("A nagyobb szám: ", b)
else:
    print("A két szám egyenlő: ", a, b)

# 3. Írja ki a program, hogy párosak-e a számok!
if a % 2 == 0:
    print("Az első szám páros: ", a)
else:
    print("Az első szám páratlan: ", a)
    
if b % 2 == 0:
    print("A második szám páros: ", b)
else:
    print("A második szám páratlan: ", b)

# 4. Írja ki a két szám összegét!
print("A két szám összege: ", a + b)
# 5. Írja ki a két szám szorzatát!
szorzat = a * b
print("A két szám szorzata: ", szorzat)