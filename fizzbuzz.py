szam = 1
celszam = 100

# for ciklus: akkor használjuk, amikor előre meg tudjuk határozoni, 
# hogy hányszor kell lefuttatni a ciklusmagot.
# formája: for i in range (1, 100):

for i in range (1, celszam + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)