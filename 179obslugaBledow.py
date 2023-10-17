#obsluga bledow TRY i EXCEPT
import sys

try:
    tasksPerPerson = 0
    tasks = 32
    personStr = input('How many persons you have?')
    persons = int(personStr)
    tasksPerPerson = tasks / persons
except ValueError:
    print("You need to enter int")
except ZeroDivisionError:
    print("Can't divide by 0")
except:
    print('Something when wrong')
else:
    print('Every person should have around %d tasks' % tasksPerPerson)

finally:
    print('Sluzy do zamkniecia calej funkcji')

