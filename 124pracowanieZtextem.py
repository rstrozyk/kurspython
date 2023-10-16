line = 'this IS a very STRANGE text'
line.capitalize() #rozpocznij text z duzej
line.title() #rozpocznij z duzej litery kazde slowo
line.lower()
line.upper()
line.swapcase() #zamien duze na male
line.replace('x','y') #zamien literki
line.count('x') #policz ile razy wystepuje
line.find('e') #na ktorej pozycji sie znajduje
line.index('e') #to samo co find
'e' in line #zwraca boolean czy wystepuje czy tez nie
line.startswith('e') #zaczyna sie litera
line.endswith('e') #konczy sie litera

import string
print(string.ascii_letters)
print(string.digits)
line.split('') #rozdzielenie tekstu ze wgledu na spacje
' '.join(list) #laczenie elementow listy do jednej listy

