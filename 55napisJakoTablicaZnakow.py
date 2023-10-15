#L55

s = 'A python script'
#print(s[2:8])  #wskazujemy które elementy tabeli wyświetlamy
print(s[:8])
print(s[8:])

message = 'A message was printed on printer: HP DESKJET'
print(message[message.find(':')+2:999])

#ZAD1
q = 'THE EYES'
print(q[0]+q[1]+q[2]+q[5]+q[3]+q[7]+q[4]+q[6])

p = 'a gentleman'
print(p[3]+p[6]+p[7]+p[2]+p[0]+p[4]+p[5]+p[1]+p[8]+p[9:])

#ZAD2

line = 'Program "Korpka nad i" nadamy o: 22:00'
time = line[line.find(':')+2:]
print(time)

tmp = line[line.find('"'):]
print(tmp)

title = line[:line.find('"')]
print(title)




