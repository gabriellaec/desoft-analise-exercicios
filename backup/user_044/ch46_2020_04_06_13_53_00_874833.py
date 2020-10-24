def numero_no_indice(lista):
    ls=[]
    for i in lista:
        if lista[i]==i:
            ls.append(lista[i])
    return ls
        