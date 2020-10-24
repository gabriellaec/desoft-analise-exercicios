def monta_mala(lista1):
    i = 0
    listanova=[]
    soma = 0
    while len(lista1) > i:
        soma += lista1[i]
        if soma<=23:
            listanova.append(lista1[i])
            i +=1
        else:
            break
    return listanova