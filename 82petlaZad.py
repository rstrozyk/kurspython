#zad1

#ZAD1
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

z = 0
zmax = len(numbers)

while z <= zmax-1:
    if (numbers[z-1])**2 == numbers[z]:
        print('Te liczby to', numbers[z-1], numbers[z])
    z += 1

#ZAD2
x=0
xmax = len(numbers)-2

while x <= xmax:
    if (numbers[x])**2 == numbers[x+1] and (numbers[x+1])**2 == numbers[x+2]:
        print(numbers[x], numbers[x+1], numbers[x+2])
    x+=1

#ZAD3
texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

t = 0
tmax = len(texts)-1

while t < tmax:
    if len(texts[t]) == len(texts[t+1]):
        print(texts[t], texts[t+1])
    t += 1

#ZAD4

cargo = [40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
boxCapacity = 90
i = 0
imax = len(cargo)

while   i < imax:
    if boxCapacity > cargo[i]:
        boxCapacity = boxCapacity - cargo[i]
    #cargo.pop(i)
    print(boxCapacity)
    i += 1

#ZAD5
s = 0
smax = 50
sum = 0

while s < smax:
    sum = s + (s+1)
    print('Suma liczba', s, s+1, 'to', sum)
    s +=1

#ZAD6
import random
my_number = random.randint(0,20)
print('\n', my_number)
guess = -1
print('Guess my number')

while guess != my_number:
    guess = int(input())
    if my_number == guess:
        print('Gratz')
    elif guess > my_number:
        print('Podana liczba jest za duza')
    else:
        print('Podana liczba jest za mala')












