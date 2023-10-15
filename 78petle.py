#petle

i=1
imax = 10

while i <= imax:
    print(i)
    i +=1
else:
    print('koniec', i)

#ZAD1

ii = 1
iimax = 31


while ii <= iimax:
    print('Row number', ii)
    ii += 1

#ZAD2

liczba = 1
liczbaMax = 13

while liczba <= liczbaMax:
    print(' \n Kwadrat liczby', liczba, 'wynosi', liczba**2)
    print('Szescian liczby', liczba, 'wynosi', liczba**3)
    liczba +=1

#ZAD4
k = 1
kmax = 10
while k <= kmax:
    print(k*'x')
    k += 1

#81
values = [10,43,12,48,12,11,18,98,57,28,19,27,49,19,74]
l=0
lmax = len(values)

while l <= lmax-3:
    if values[l+2] > values[l+1] and values[l+1] > values[l]:
        print('Liczby rosna od', values[l])
    l += 1

