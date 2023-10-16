#funkcje

def PrinmtHello():
    #ta funckja pisze hello
    print('Hello')
    return

PrinmtHello()



#ZAD1

def PrintCat():
    txt = r'''
    |\---/|
    | o_o |
     \_^_/'''
    print(txt)
    return
PrintCat()

def PrintBear():
    txt = r'''
    /  \.-"""-./  \
    \    -   -    /
     |   o   o   |
     \  .-'"'-.  /
      '-\__Y__/-'
         `---`'''
    print(txt)
    return

PrintBear()

def PrintBat():
    txt = r'''
       /\                 /\
      / \'._   (\_/)   _.'/ \
     /_.''._'--('.')--'_.''._\
     | \_ / `;=/ " \=;` \ _/ |
      \/ `\__|`\___/`|__/`  \/
              \(/|\)/       '''
    print(txt)
    return

PrintBat()

#ZAD2
def DaysToEndOfYear():
    from datetime import date
    date_today = date.today()
    current_year = date_today.year
    date_end_year = date(current_year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)


DaysToEndOfYear()

#ZAD 3

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
    elif animal == 'bear':
        print(bear)
    else:
        print(bat)
    return
PrintAnimal1('cat')


