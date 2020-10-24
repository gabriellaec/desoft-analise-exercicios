def quantos_uns(lista):
    lista = str(lista)
    i = 0
    lista2 = []
    while i < len(lista):
        if lista[i] == '1':
            lista2.append(lista[i])
        i += 1
    return len(lista2)
        