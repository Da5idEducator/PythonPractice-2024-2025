import random

gyumolcsok = [
    "narancs",
    "cseresznye",
    "alma",
    "dinnye",
    "eper",
    "málna",
    "szőlő",
    "banán",
    "szilva",
    "körte"
]


MercedesModellek = [
    "E55 AMG",
    "C63 AMG",
    "GT 63",
    "S63",
    "Maybach",
    "G63",
    "C220",
    "Vito",
    "Sprinter",
    "CLK GTR"
]

def sorsolas(gyumolcslista, tarcsak):
    roll = []
    
    for i in range(0, tarcsak):
        random.shuffle(gyumolcslista)
        roll.append(gyumolcslista[0])
    
    return roll

def pontozas(roll):
    Elemek = set()
    Azonos = []
    
    for i in roll:
        if i in Elemek:
            Azonos.append(i)
        else:
            Elemek.add(i)
    
    return len(Azonos)
    
    
def tesztSorsolas(tesztekSzama, tarcsakSzama, adatLista):
    pontszamElofordulas = []
    for i in range (0, tesztekSzama):
        vizsgaltSorsolas = sorsolas(adatLista, tarcsakSzama)
        vizsgaltPontszam = pontozas(vizsgaltPontszam)
        pontszamElofordulas[i] = pontszamElofordulas[i] + 1
        
    
kisorsoltGyumolcsok = sorsolas(gyumolcsok, 3)
gyumolcsPontok = pontozas(kisorsoltGyumolcsok)

print(kisorsoltGyumolcsok)
print("A sorsolás pontszáma: ", gyumolcsPontok)

kisorsoltAutok = sorsolas(MercedesModellek, 4)
autoPontok = pontozas(kisorsoltAutok)

print(kisorsoltAutok)
print("A sorsolás pontszáma", autoPontok)


egyPontos = 0
ketPontos = 0

for i in range (0, 1000000):
    
    vizsgalt = sorsolas(gyumolcsok, 3)
    vizsgaltPontszam = pontozas(vizsgalt)
    
    if vizsgaltPontszam == 1:
        egyPontos = egyPontos + 1
    elif vizsgaltPontszam == 2:
        ketPontos = ketPontos + 1
        
print("Egy pontos sorsolások", egyPontos)
print("Két pontos sorsolások: ", ketPontos)
