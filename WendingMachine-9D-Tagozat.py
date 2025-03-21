import random

my_file = open("WendingMachineItems.txt", "r", encoding="utf-8")
#print(my_file)

raw_data = my_file.read()
#print(raw_data)
my_file.close()

automataItems = raw_data.replace('\n', '').split(',')
#print(automataItems)

# 1 Automata tartalmának listázása
def ListAutomata(tartalom):
    # Listázás számokkal
    print("Az automata tartalma:")
    sorszam = 0
    for i in tartalom: 
        sorszam = sorszam + 1
        print(sorszam, i)
    
    mainMenu()
        
    

# 2 Vásárlás az automatából
def BuyAutomata(tartalom):
    # Vásárlás
    print("Melyik terméket választod?")
    #ListAutomata(tartalom)
    valasztott = int(input("Választás száma: "))
    
    print("_______________")
    print("               ")
    print(tartalom[valasztott-1])
    print("               ")
    print("_______________")
    tartalom.pop(valasztott-1)
    mainMenu()

# 3 Új termék betöltése az automatába
def AddAutomata(tartalom):
    # Termék belehelyezése
    print("Új termék elhelyezése az automatába")
    
    newItem = input("Mit szeretne az automatába helyezni?: ")
    tartalom.append(newItem)
    mainMenu()

# 4 A termékek ABC sorrendbe rendezése
def ABCAutomata(tartalom):
    # ABC sorrendbe helyezés
    print("ABC sorrendbe rendezzük az automata tartalmát")
    tartalom.sort()
    mainMenu()

# 5 A termékek véletlenszerű sorrendbe rendezése
def RandomizeAutomata(tartalom):
    # Véletlenszerű sorrend
    print("Véletlenszerű sorrendbe rendezzük az automata tartalmát")
    random.shuffle(tartalom)
    mainMenu()

# 6 Főmenü - számokkal választható
def mainMenu():
    valasztottMenupont = 0
    print("Üdvözlöm!")
    print("Kérem, válasszon az alábbi lehetőségek közül:")
    print("1 - Mi van az automatában?")
    print("2 - Vásárlás")
    print("3 - feltöltés")
    print("4 - ABC sorrendbe helyezés")
    print("5 - Véletlen sorrendbe helyezés")
    
    valasztottMenupont = int(input("Választás: "))
    
    if valasztottMenupont == 1:
        ListAutomata(automataItems)
    elif valasztottMenupont == 2:
        BuyAutomata(automataItems)
    elif valasztottMenupont == 3:
        AddAutomata(automataItems)
    elif valasztottMenupont == 4:
        ABCAutomata(automataItems)
    elif valasztottMenupont == 5:
        RandomizeAutomata(automataItems)
    else:
        print("Ön lehetetlent választott!")
        mainMenu()
    

mainMenu()