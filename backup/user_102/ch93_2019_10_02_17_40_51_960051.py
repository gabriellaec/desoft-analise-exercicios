def verifica_numero(x):
    lista = []
    x = str(x)
    for i in x:
        lista.append(i)
    i = 0
    lista1 = []
    while i < len(lista):
        lista1.append(int(lista[i]))
        i += 1
    e = 0
    soma = 0
    while e < len(lista1):
        soma += lista1[e]**lista1[e]
        e += 1
    if int(x) == soma:
        return True
    else:
        return False
