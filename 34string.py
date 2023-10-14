#L34 String

atext = 'this is a text'
print(atext.capitalize())   #wymuszenie rozpoczecia z wielka litera
print(atext.endswith('ext')) #sprawdzenie czy kończy sie danym czlonem
print(atext.endswith('sasdxt'))
print(atext.isupper())      #sprwadzenie czy jest napisany wielkimi
atext.upper()
print(atext.upper().isupper())
print(atext.find('is'))     #sprawdzenie na którm znaku sa literki
print(atext.find('is', 3))  #rozpoczecie szuakania od konkretnej litery
print(atext.replace('a', '4').replace('s', '7').replace('i','1'))
print(atext.split(' '))
losowyNumer = '1000'
print(losowyNumer.isdigit())  #czy jest liczba
print(losowyNumer.isdecimal()) #czy jest liczba przecinkowa
print(losowyNumer.isalpha()) #czy sa tylko litery
print(losowyNumer.isalnum()) #czy sa tylko numerki i cyfry


#ZAD 1
quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'
print(quote.upper())
print(quote.lower())
print(quote.endswith('street'))
print(quote.upper().isupper())
print(quote.find('one'))
print(quote.replace('one', '1'))
print(quote.replace('one', '1').replace('both', '2'))
print(quote.split(' '))
print(quote.isalnum())