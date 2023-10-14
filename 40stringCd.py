#String cz. 3

number = '1000'
print(int(number) + 1)

print(type(number))

number1 = '1000'
print(type(number1))


#ZAD 1

article = '''
In 1974, Monthy python between production on the third and fourth seasons, the group decided to embark on their first "proper" feature film, containing entirely new material. Monty Python and the Holy Grail was based on Arthurian legend and was directed by Jones and Gilliam. Again, the latter also contributed linking animations (and put together the opening credits). Along with the rest of the Pythons, Jones and Gilliam performed several roles in the film, but Chapman took the lead as King Arthur. Cleese returned to the group for the film, feeling that they were once again breaking new ground. Holy Grail was filmed on location, in picturesque rural areas of Scotland, with a budget of only £229,000; the money was raised in part with investments from rock groups such as Pink Floyd, Jethro Tull, and Led Zeppelin, as well as UK music industry entrepreneur Tony Stratton Smith (founder and owner of the Charisma Records label, for which the Pythons recorded their comedy albums).[68]
The backers of the film wanted to cut the famous Black Knight scene (a Sam Peckinpah send-up in which the Black Knight loses his limbs in a duel), but it was eventually kept in the movie.[69] "Tis but a scratch" and "It's just a flesh wound…" are often quoted.[70] Holy Grail was selected as the second-best comedy of all time in the ABC special Best in Film: The Greatest Movies of Our Time. and viewers in a Channel 4 poll placed it sixth.[71]
'''
print(article)

#ZAD3
print(article.upper())

print(article.lower().replace('monthy', 'flying'))

#ZAD5
print(article.split(' '))

#ZAD6
print('Word python appears', article.count('python'), 'times')

#ZAD7
print('to print the \\ you need to put \\ twice in your text like this: \\\\')

#ZAD8
print("The best hits of '80s!!!")

#ZAD9
PLN = 234

print('\n','cur','\t','exchange','\t','ammount')
print('USD','\t','3.65','\t',PLN/3.65)
print('EUR','\t','4.23','\t',PLN/4.23)

#ZAD 10
valueAsText = 123.45
factor = 1.23
print('value is ', valueAsText, 'factor is', factor, 'value*factor=', float(valueAsText)*factor)