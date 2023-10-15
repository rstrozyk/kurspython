#for in range
import random
list = []
for number in range (1,21):
    list.append(random.randint(0, 100))

print(list)
parzyste = []
lista = [0,1,2,3,4]
for num in lista:
    print(lista[num])


#ZAD1
string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

#for numb in range (0,10):
    #print(string_A)

for numb in range (1,10):
    if numb % 2 !=0:
        print(string_A)
    else:
        print(string_B)
