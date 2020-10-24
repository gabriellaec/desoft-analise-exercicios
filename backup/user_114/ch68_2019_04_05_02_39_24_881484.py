def separa_trios(lista_total):
    i=0
    trios=[]
    while i<len(lista_total):
        trio=lista_total[i:i+3]
        trios.append(trio)
        i=i+3
    return trios   