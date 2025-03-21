import random

my_file = open("reformatus.txt", "r", encoding="utf-8")
data = my_file.read()
print(data)
gyumolcsok = data.replace('\n', ' ').split(',')
print(gyumolcsok)

def leltar(my_list):
    sorszam = 1
    for i in my_list:
        print(sorszam, i)
        sorszam = sorszam + 1

leltar(gyumolcsok)