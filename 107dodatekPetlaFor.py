#ciag fibonnacciego

fibonacciIterations = 20
a1 = 0
a2 = 1
a3 = 0
for i in range(0,fibonacciIterations):
    print('Step',i,'value',a3)
    a1=a2
    a2=a3
    a3=a1+a2
print('-------------------------------------------------')


#Zad2
Text = 'Industrial Light & Magic: In this case, you find Python used in the production process for scripting complex, computer graphic-intensive films. Originally, Industrial Light & Magic relied on Unix shell scripting, but it was found that this solution just couldn’t do the job. Python'
TextSplit = Text.split(' ')
for words in TextSplit:
    if words.__contains__('p') or words.__contains__('P'):
        print(words)

#Zad3
dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less than 50%'}

for object in dictionary:
    print(object,'-', dictionary[object])