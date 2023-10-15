#Ternary

itRains = False
if itRains:
    print('We stay at home')
else:
    print("We go out")


print('We stay') if itRains else print('We go out')

#ZAD1

musclePain = True
fever = True
weakness = True

print('Suspiction of influenza') if musclePain and fever and weakness else print('Flu is unlikely')

