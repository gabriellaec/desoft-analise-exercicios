lista = [0]
i = 0
while True:
    a = int(input('x'))
    if a == 0 or a <= 0:
        break
    lista[i] = a
    lista += [0]
    i += 1
b = len(lista)
j = b
while j > 0:
    print(lista[j-1])
    j = j - 1
    
    