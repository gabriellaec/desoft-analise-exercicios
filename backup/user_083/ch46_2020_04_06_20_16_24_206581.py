def numero_no_indice(lista):
    i=0
    r=[]
    for i in range(len(lista)):
        if lista[i] == 1:
            r.append(i)
            i+=1
        else:
            i+=1
    return r