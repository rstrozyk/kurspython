#zwracanie wartosci funkcji

def potegowanie(x,y):
    potega = x**y
    return potega #bez returnowania potegi funkcja nic nie zwroci wiec print nic nie wydrukuje

print(potegowanie(5,2))

#ZAD1

def PrintAnimal1(animal):

    cat = r'''
      |\---/|
      | o_o |
       \_^_/'''

    bear = r'''
        /  \.-"""-./  \
        \    -   -    /
         |   o   o   |
         \  .-'"'-.  /
          '-\__Y__/-'
             `---`'''
    bat = r'''
       /\                 /\
      / \'._   (\_/)   _.'/ \
     /_.''._'--('.')--'_.''._\
     | \_ / `;=/ " \=;` \ _/ |
      \/ `\__|`\___/`|__/`  \/
              \(/|\)/       '''
    if animal == 'cat':
        print(cat)
        return True
    elif animal == 'bear':
        print(bear)
        return True
    elif animal == 'bat':
        print(bat)
        return True
    else:
        print('Lack of parameter')

print(PrintAnimal1('asd'))
