import random

#stworzenie liczby
list = []

for number in range (0,10):
    list.append(random.randint(0,99))
print(list)


#rozwiazanie lopatologiczne - wypisanie parzystych
parzyste = []
k = 0
while k < len(list):
    if list[k] %2 == 0:
        parzyste.append(list[k])
    k += 1
print(parzyste)

#rozwiazanie 2, nie dzialajace
parzyste1 = []
for num in list:
    if list[num] %2 == 0:
        parzyste1.append(list[num])
print(parzyste1)