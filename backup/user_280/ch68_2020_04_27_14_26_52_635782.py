def separa_trios(lista):
    lista2 = []
    if len(lista) == 1:
        lista2.append(lista[0])
    if len(lista) == 2:
        lista2.append(lista[0])
        lista2.append(lista[1])
    if len(lista)>=3 and len(lista)%3 == 0:
        i=0
        while i<len(lista):
            lista2.append(lista[i::3])
            i+=3
    if len(lista)>=3 and len(lista)%3 == 1:
        i=0
        while i<len(lista):
            lista2.append(lista[i::3])
            i+=3
        lista2.append(lista[-1])
    if len(lista)>=3 and len(lista)%3 == 2:
        i=0
        while i<len(lista):
            lista2.append(lista[i::3])
            i+=3
        lista2.append(lista[-2])
        lista2.append(lista[-1])
    return lista2