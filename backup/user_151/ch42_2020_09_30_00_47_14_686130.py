lista = [0]
i = 0
while True:
    y = input('x')
    lista += [0]
    if y != 'fim':
        lista[i] = y
    else:
        lista[i] = y
        break
j = len(lista)
z = 0
while z < j:
    w = str(lista[z])
    if w[0] == 'a':
        print(lista[z])
    z += 1
    
    
    
    