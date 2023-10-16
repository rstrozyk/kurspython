#lotto

import random

numery = []
while len(numery) < 7:
    nowyNumer = random.randint(1,49)
    if nowyNumer in numery:
        continue
    numery.append(nowyNumer)

print(numery)