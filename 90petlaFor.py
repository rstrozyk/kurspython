#petla for

persons = ['Elize', 'Steven', 'Seba', 'Margaret', 'Svetlana', 'Raphael']

domain = 'mycompany.com'

for person in persons:
    email = person + '@' + domain
    print(email)

#ZAD1

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for element in data:
    element = element.upper()
    #print(element)

#ZAD2
elements = []

for element in data:
    elements = element.split((':'))
    if elements[0] == 'Error':
        print(elements[0].upper(), elements[1].upper())
    else:
        print(elements[0].upper(), elements[1])









