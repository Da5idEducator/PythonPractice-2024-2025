# A program bekéri a születési évet
# valamint az aktuális évet,
# majd kiszámítja az életkort.

szuletesiEv = int(input("Melyik évben születtél?: "))
print(type(szuletesiEv))
szuletesnap = input("Volt már születésnapod ebben az évben? I/N: ")

eletkor = 2025 - szuletesiEv

if not(szuletesnap == "i" or szuletesnap == "I"):
    eletkor = eletkor - 1
    
print("A válaszaid alapján te most", eletkor, "éves vagy.")
