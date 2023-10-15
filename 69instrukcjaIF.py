#instrukcja warunkowa IF

age = 19
isDrunk = True
isRestrictedArea = True
if age >= 18 and not isDrunk and not isRestrictedArea:
    print('Mozesz kupic alkohol')
else:
    print('Nie sprzedam Ci alkoholu')

#ZAD1
likesNeeded = 500
sharesNeeded = 100
likes = 5555
shares = 5555

discount = 0.9

if likes >= likesNeeded and shares >= sharesNeeded:
    print('Otrzymujesz promke')
else:
    print('Nie spelniono warunkow promki')

#ZAD2
isPizzaOrdered = True
isBigDrinkOrdered = True
isWeekend = False

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('Otrzymujesz kupon')
else:
    print('Nie otrzymujesz kuponu')

#ZAD3
diskSize = 140
diskSizeUsed = 144
fileSize = 1

if fileSize <= (diskSize-diskSizeUsed):
    print("Mozna zapisac")
else:
    print("Za malo miejsca")

