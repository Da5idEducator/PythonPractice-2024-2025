import random

pontszam = 0
valasz = "i"

roll = []
nyeroKombinacio = []

def nyeroKombo(roll):
    marVolt = set()
    tobbszoros = []
    
    for i in roll:
        if i in marVolt:
            tobbszoros.append(i)
        else:
            marVolt.add(i)
    if len(tobbszoros) > 1:
        azonosLapokSzama = 2
    elif len(tobbszoros) > 0:
        azonosLapokSzama = 1
    else:
        azonosLapokSzama = 0
        
    return azonosLapokSzama

def eredmenyKiiras(jatekokszama, ketAzonos, haromAzonos):
    print("Játékok száma: ", jatekokszama)
    print("Két azonos gyümölcs: ", ketAzonos)
    print("Három azonos gyümölcs: ", haromAzonos)
    
def jatekKiiras(sorsolas):
    print(sorsolas[0], sorsolas[1], sorsolas[2])

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

def jatek(jatekokSzama, szamlalo = 0):
    ketAzonosGyumolcs = 0
    haromAzonosGyumolcs = 0
    
    while szamlalo < jatekokSzama:
        szamlalo = szamlalo + 1
        for i in range (0, 3):
            random.shuffle(gyumolcsok)
            roll.append(gyumolcsok[0])
    
        jatekKiiras(roll)
        
        kombinaciok = nyeroKombo(roll)
        if kombinaciok == 1:
            ketAzonosGyumolcs = ketAzonosGyumolcs + 1
        elif kombinaciok == 2:
            haromAzonosGyumolcs = haromAzonosGyumolcs + 1
        
        roll.clear()
        
    eredmenyKiiras(szamlalo, ketAzonosGyumolcs, haromAzonosGyumolcs)
        
        
jatek(10)
