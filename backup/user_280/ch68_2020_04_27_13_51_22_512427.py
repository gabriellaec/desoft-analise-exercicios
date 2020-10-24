def separa_trios(lista):
    lista2 = []
    i=0
    while i<len(lista):
        lista2.append(lista[i::3])
        i+=3