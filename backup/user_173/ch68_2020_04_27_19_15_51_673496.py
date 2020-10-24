def separa_trios(lista1):
    lista2 = []
    i = 0
    while i < len(lista1):
        lista2.append(lista1[i])
        lista2.append(lista1[i+1])
        lista2.append(lista1[i+2])
    i += 1
    return lista2
   