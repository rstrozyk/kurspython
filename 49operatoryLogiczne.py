#Operatory logiczne

isWeekend = True
print('Is weekend = ', isWeekend)

temperature = 22
print('Temperature =', temperature)

toDoList = ''
print('To Do =', toDoList)

isHappy = isWeekend and temperature > 20 and toDoList == '' or not isWeekend and temperature < 20 and toDoList != ''
print('Is happy?', isHappy)

# != nie rowna sie
# >= wieksze rowne
# == porownanie
# and - koniunkcja
# or - alternatwya

#ZAD 1
isAutomaticMode = True
is80PercentLight = True
isDirectLight = False
isRainy = False
turnLightsOn = isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)

print('Automatic mode', isAutomaticMode)
print('Is the light good', is80PercentLight)
print('Is sun low', isDirectLight)
print('Is it rainy', isRainy)
print("TURN LIGHTS ON", turnLightsOn)
