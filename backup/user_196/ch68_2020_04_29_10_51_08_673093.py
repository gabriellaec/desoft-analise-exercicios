def separa_trios(lista):
    lista_trios=[]
    i=0
    while i < len(lista):
        listatrios.append(lista[i:i+3:3])
        i+=3
    return listatrios