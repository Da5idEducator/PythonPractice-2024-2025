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

roll = []

for i in range (0, 3):
    random.shuffle(gyumolcsok)
    roll.append(gyumolcsok[0])
    

ismetlodo = []
marVolt = set()

# roll = ["körte", "körte", "körte"]
for i in roll:
    if i in marVolt:
        ismetlodo.append(i)
    else:
        marVolt.add(i)
    
print(roll)
print("Ismétlődő elemek: ", ismetlodo)
print("Ismétlődő elemek száma: ", len(ismetlodo))
