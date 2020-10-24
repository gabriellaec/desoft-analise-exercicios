def numero_no_indice(lista):
    i=0
    f=[]
    while i<len(lista):
        if lista[i]==i:
            f.append(lista[i])
        else:
            pass
        i+=1
    return f