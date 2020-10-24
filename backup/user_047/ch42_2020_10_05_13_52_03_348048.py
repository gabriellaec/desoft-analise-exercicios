z =[]
contador = 0
a = 0
s = []
while a != 'fim':
    z.append(input('digite sua palavra'))
    a = z[contador]
    if z[contador][0]=='a':
        s.append(z[contador])
    contador +=1
print(s)