import random

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

def sorsolas(targyak, tarcsakSzama):
    eredmeny = []
    
    for i in range (0, tarcsakSzama):
        random.shuffle(targyak)
        eredmeny.append(targyak[0])
        
    return eredmeny


def pontozas(eredmenyLista):
    pontszam = 0
    voltmar = set()
    ismetlodo = []
    
    for i in eredmenyLista:
        if i in voltmar:
            ismetlodo.append(i)
        else:
            voltmar.add(i)
    
    pontszam = len(ismetlodo)
    return pontszam
    
    
def teszt(lista, tarcsak, tesztesetek):
    nyeremenyek = [tarcsak-1]
    print(nyeremenyek)
    
    for i in nyeremenyek:
        nyeremenyek.append(0)
    
    for i in range(0, tesztesetek):
        roll = sorsolas(lista, tarcsak)
        pontszam = pontozas(roll)
        for i in nyeremenyek:
            nyeremenyek[i] = nyeremenyek[i] + 1
    

roll = sorsolas(gyumolcsok, 4)
pontszam = pontozas(roll)

print("Sorsolás eredménye:", roll)
print("Pontszám:", pontszam)

egyPontos = 0
ketPontos = 0
haromPontos = 0

for i in range(0, 100000):
    
    roll = sorsolas(gyumolcsok, 4)
    pontszam = pontozas(roll)
    print(roll)
    
    if pontszam == 1:
        egyPontos = egyPontos + 1
    elif pontszam == 2:
        ketPontos = ketPontos + 1
    elif pontszam == 3:
        haromPontos = haromPontos + 1

print("Két találatosok: ", egyPontos)
print("Három találatosok: ", ketPontos)
print("Négy találatosak: ", haromPontos)