lista = [0]
i = 0
while True:
    y = input('x')
    if y != 'fim':
        lista[i] = y
    else:
        lista[i] = y
        break
    i += 1
    lista += [0]
j = len(lista)
z = 0
print(lista)
while z < j:
    w = str(lista[z])
    if w[0] == 'a':
        print(lista[z])
    z += 1


    
    
    
    
    
    
    