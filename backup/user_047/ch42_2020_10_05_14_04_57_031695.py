a = 0
s = []
contador = 0
while a != 'fim':
    z = input('digite sua palavra')
    a = z
    if z[0]=='a':
        s.append(z)
    contador +=1    
print(s)