lista = []

while True:
    i = int(input("A"))
    
    if i <= 0:
        break
    lista.append(i)

if len(lista) < 2:
    print(lista)
else:
    i = len(lista) - 1
    result = []
    
    while i >= 0:
        result.append(lista[i])
        i = i - 1
    print(result)