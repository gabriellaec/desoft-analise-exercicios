def separa_trios(lista):
    lista_trios=[]
    i=0
    while i<len(lista):
        trio=[]
        while len(trio)<3 and i<len(lista):
            trio.append(lista[i])
            i+=1
        lista_trios.append(trio)
    return lista_trios