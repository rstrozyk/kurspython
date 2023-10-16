#ZAD1

percent = 0.03
maxTimeYears = 10
capital = 20000
y = 1

while y <= maxTimeYears:
    capital += capital * percent
    print('Capital after %d years is %d' % (y, capital))
    y += 1

#ZAD2
number = 1234567
x = 0
sum = 0
while x < number > 0:
    sum = sum + (number % 10)
    number = (number // 10)
    print(sum)
    x +=1