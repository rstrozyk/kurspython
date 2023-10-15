#zagniezdzone For

for x in range (1,6):
    line = str(x)
    for y in range (1,6):
        line += ('%3d' % (x*y))
    print(line)


#ZAD 1
i = 10
result = 1

for j in range(1, i + 1):
    result = result + result*j

print(i, result)

print('------------')

#ZAD2

x = 10

for i in range(1, x + 1):

    result = 1

    for j in range(1, i + 1):
        result = result + result *j

    print(i, result)

print('------------')

#ZAD3
list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for element in list_noun:
    for element1 in list_adj:
        print(element1 +' '+ element)