def separa_trios(lista):
    lista_tds_trios=[]
    i=0
    j=0
    lista_trios=[]
    while i<len(lista):
        lista_trios.append(lista[i])
        j+=1
        if j==3:
            lista_tds_trios.append(lista_trios)
            lista_trios=[]
            j=0
        i+=1
    if 0<j<3:
        lista_tds_trios.append(lista_trios)
    return lista_tds_trios