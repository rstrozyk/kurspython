#Formatowanie napisow, zastepowanie wyrazow w tekscie

message1 = 'Processing file %s'
print(message1 % ('file.txt'))

message2 = 'File %s has size of %dKB'
print(message2 % ('file.txt', 100))

message3 = 'File %20s has size of %10d KB'  #rezerwujemy konkretna ilosc znakow dla zmiennych
print(message3 % ('file.txt', 100))

message4 = 'Processing file {0:s}'
print(message4.format('file.txt'))

message5 = 'File {0:s} has {1:d}'
print(message5.format('file.txt', 5))

#ZAD 1
helloMessage = 'Hello %s!'
helloMessage1 = 'Hello {0:s}!'
print(helloMessage % 'Kate')
print(helloMessage1.format('Chis'))

helloMessage2 = '%s has %d %s'
print(helloMessage2 % ('Kate', 1, 'animal'))

helloMessage3 = '{0:s} has {1:d} {2:s}'
print(helloMessage3.format('Chris', 1, '$'))

#ZAD 2
line = '%20s costs %6d €'
print(line % ('ICE CREAM', 3))
print(line % ('TRIP TO VENICE', 119))
print(line % ('PIZZA HAWAI', 6))

line1 = '{0:s} {1:d}'

print(line1.format('ICE CREAM', 3))
print(line1.format('TRIP TO VENICE', 119))
print(line1.format('PIZZA HAWAII', 6))