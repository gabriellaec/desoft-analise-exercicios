def numero_no_indice(lista):
    ls=[]
    x=len(lista)
    for i in range(lista):
        if lista[i]==i:
            ls.append(lista[i])
    return ls
        