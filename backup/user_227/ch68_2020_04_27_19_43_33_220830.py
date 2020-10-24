def separa_trios(lista):
    lista_trios=[]
    i=0
    while i<len(lista):
        trio=[]
        while len(trio)<3:
            trio.append(lista[i])
        lista_trios.append(trio)
        i+=1
    return lista_trios