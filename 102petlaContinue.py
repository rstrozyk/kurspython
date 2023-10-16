#instrukcja continue

persons = ['Elize', 'Steven@sales.mycompany.com', 'Seba', 'Margaret', 'Svetlana@mycompany.com', 'Raphael']

domain = 'mycompany.com'

emails = []
''''
for person in persons:
    if '@' in person:
        emails.append(person)
    else:
        email = person + '@' +domain
        emails.append(email)
print(emails)'''

for person in persons:
    if '@' in person:
        emails.append(person)
        continue

    email = person + '@' +domain
    emails.append(email)
print(emails)
