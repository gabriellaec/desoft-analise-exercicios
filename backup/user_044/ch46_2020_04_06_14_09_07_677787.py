def numero_no_indice(lista):
    ls=[]
    x=len(lista)
    for i in range(x):
        if lista[i]==i:
            ls.append(lista[i])
    return ls
        