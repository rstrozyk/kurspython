'''
Ten skrypt policzy ile razy mrugniemy okiem w czasie X lat
Zakladamy, ze:
-liczba mrugniec na min to 20
-liczba minut w godzine to 60
-liczba godzin w dobie to 24
-liczba lat X
-Jesli spimy 8 godzin to liczba godzin w dobie to 16
'''

#liczba mrugniec w minute
blinksPerMin = 20

#liczba minut w godzinie i w dobie
minInHour = 60
hoursInDay = 16
daysInYear = 365

#liczba lat
years = 50

#liczba mrugniec w X lat
blinksNumber = blinksPerMin*minInHour*hoursInDay*daysInYear*years
print(blinksNumber)

#ZADANIE 2- zdefiniowac tekst i zapisac go wielkimi literami oraz rozdzielic, podaj dlugosc listy
box = 'cola:9 bottles:1 liter'
print(box.upper())
boxSplit = box.split(':')
print(boxSplit)
print(len(boxSplit))

#ZADANIE 3 - oblicz pole kola

WartoscPi = 3.14
PromienOkregu = 5
PoleKola = WartoscPi*PromienOkregu**2
print("Pole kola to:", PoleKola)

#obwod kola
ObwodKola = 2*WartoscPi*PromienOkregu
print("Obwod kola to:", ObwodKola)

#pole prostokata
a = 10
b = 5
PoleProstokata = a*b
print("Pole prostokata to:", PoleProstokata)

#poletrapezu
h = 10
PoleTrapezu = (a+b)*h/2
print("Pole trapezu to:", PoleTrapezu)
