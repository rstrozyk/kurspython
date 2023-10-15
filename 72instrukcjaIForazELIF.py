#instruikcja elif

age = 19
isDrunk = False
isRestrictedArea = False

if age < 18:
    print('Jestes za mlody')
elif isDrunk:
    print('Jestes pijany')
elif isRestrictedArea:
    print('Jestes w restricted area')
else:
    print('Mozesz kupic')

#ZAD 1
likesNeeded = 500
sharesNeeded = 100
likes = 5
shares = 55

if likesNeeded > likes:
    print('Nie masz wystarczajaco lajkow')
elif sharesNeeded > shares:
    print('Nie masz wystarczajaco sharow')
else:
    print('Dostajesz promke')