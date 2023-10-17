# 1. Utworzyc liste 10 elementow
# 2. Wypisac z listy elementow parzystych
# 3. Utworzenie funkcji z argumentami, ktora zrobi to co w 1 i 2

import random

#Zad1
'''lenght = 10
list = []

for i in range(lenght):
    list.append(random.randint(0,999))
print(list)

#Zad2
listEven = []
for k in range(lenght):
    if list[k] % 2 != 0:
        listEven.append(list[k])
print(listEven)'''

#Zad3
def createListOfEvens(lenght,min,max):
    listEven = []
    while len(listEven) < lenght:
        number = random.randint(min,max)
        if number % 2 == 0:
            listEven.append(number)
    print(listEven)

createListOfEvens(10,0,9999)



