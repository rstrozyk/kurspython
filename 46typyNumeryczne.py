#typy numeryczne
import sys

wynik = 5/3
print(type(wynik))
print(sys.maxsize)

#inny operator dzielenia
wynik1 = 5//3     #dzielenie calkowice
print(wynik1)

wynik2 = 5 % 3      #reszta z dzielenia
print(wynik2)

print(float('inf')>9999) # float('inf') to nieskonczonosc
print(type(float('inf')))


#ZAD1
name = 'Rafal'
age = 30
daysInYears = 365
message = '{0:s} is {1:d} years old, so its about {2:d} days old'
print(message.format(name, age, daysInYears*age))

#ZAD2
resztaZDzielenia = 1234567890 % 12345
print(resztaZDzielenia)

dzielenieBezReszty = 1234567890 // 12345
print(dzielenieBezReszty)