import random

print('Random int', random.randint(1,100))

list = ['KO', 'PIS', 'LEW', '3D', 'BEZ', 'KONF']
print('Choosing random number form a range', random.choice(list))
print(random.randrange(1,100))

shuffledList = []
shuffledList.append(random.shuffle(list))
print(shuffledList)

print(random.random())

#GENEROWANIE HASLA
lista = []
for i in range (32,127):
    lista.append(chr(i))
print(lista)

dlugoscHasla = 10
haslo = ''
while haslo.__contains__('A') != True: #zapewniamy, ze bedzie tam litera A
    haslo = ''
    for k in range (dlugoscHasla):
        haslo += random.choice(lista)
print(haslo)