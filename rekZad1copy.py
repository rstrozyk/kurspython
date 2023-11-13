#stworzyc liste elementow liczb losowych
import random

list = []
def createList(lenght,min,max):

    while len(list) < lenght:
        number = random.randint(min,max)
        if number % 2 == 0:
            list.append(number)
        continue
    return list
createList(10,1,100)
print(list)
