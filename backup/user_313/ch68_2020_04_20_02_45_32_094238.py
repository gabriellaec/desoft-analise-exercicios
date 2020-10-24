def separa_trios(l1):
    lista = list()
    for i in range(3,len(l1)+3,3):
        lista.append(l1[i-3:i])
        
    return(lista)