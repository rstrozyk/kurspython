#listy

countries = ['FR', 'US', 'DE', 'RU']
countries[1] = 'GB'
print(countries[1])

countries.append('PL') #dodawanie elementu na koncu listy
countries.insert(2,'SWE') #dodwaniae w konkrentym miejscu
countries.remove('RU') #usuwanie elementu
countries.sort()        #sortowanie
countries.reverse()     #odwrocenie listy
print(countries)
print(countries.pop(2))    #wyjmowanie elementu i usuwanie
print(countries.index('PL')) #sprawdzenie na ktorym indeksie jest objekt
print(countries.count('PL'))    #liczy ile razy wystepuje na liscie
print(countries)

countries1 = ['FI','IT']
countries.extend(countries1) #dodwanie listy
print(countries)

countries2 = countries.copy() #kopiowanie
print(countries2)
countries2.clear()
print(countries2)

#ZAD1
hitsTitles = ['BIN', 'BR', 'STH', 'ROTS', 'WYWH']
hitsTitles.append('CIT')
hitsTitles.append('AGA')
print(hitsTitles)

hitsTitles.insert(2,'HC')
print(hitsTitles)

hitsTitles.insert(0,'TSOS')
print(hitsTitles)

print(hitsTitles.index('HC'))

hitsTitles.remove('HC')
print(hitsTitles)

hitsTitles[0] = 'ETS'
print(hitsTitles)

hitsToRead = hitsTitles.copy()
print(hitsToRead)

hitsToRead.reverse()
print(hitsToRead)

hitsToRead.sort()
print(hitsToRead)

additionalsSongs = ['NTC2', 'WUWH']
hitsToRead.extend(additionalsSongs)
print(hitsToRead)

print(hitsToRead.count('WUWH'))
print(hitsToRead.count('ROTS'))
hitsToRead.clear()
print(hitsToRead)


