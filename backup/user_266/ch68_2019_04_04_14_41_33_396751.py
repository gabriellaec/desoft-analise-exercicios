def separa_trios(lista):
    i=0
    lista_trios=[]
    while i<len(lista):
        lista_trios.append(lista[i:i+3])
        i+=3
    return lista_trios