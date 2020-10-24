def numero_no_indice(x):
    lista=[]
    i=0
    while i<len(x):
        if  x[i]==i:
            lista.append(x[i])
        i=i+1
        return lista