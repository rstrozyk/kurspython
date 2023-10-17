#wlasna funkcja switch

def WeekdayInFrench(dayNumber):

    names = {
        0 : 'Monday',
        1 : 'Tuesday',
        2 : 'Weendsday'
    }

    return names.get(dayNumber, 'error')

print(WeekdayInFrench(2))


#Zad1
def GiveGeomSeqElement(a1 = 3, factor = 2, index = 10):
    #funckcja oblicza wartosc elementu index dla ciagu geometrycznego dla a1, ilorazu (factor)

    wynik = a1 * factor**(index -1)
    return wynik

print(GiveGeomSeqElement())

#ZAD2

len = 10
a = 3
q = 2
sum = 0

for i in range(0,len):
    an = a * q**(i)
    sum += an

    print(an, sum)
