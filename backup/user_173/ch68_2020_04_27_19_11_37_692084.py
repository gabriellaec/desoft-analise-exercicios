def separa_trios(lista1):
    lista2 = []
    i = 0
    while i < (len(lista1)-2):
        if i > 0:
            lista2.append(lista[i],lista[i+1],lista[i+2])
    i += 1
    return lista2
   