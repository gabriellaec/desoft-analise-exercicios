def numero_no_indice(lista):
    l=[]
    for i in range(len(lista)):
        if i==lista[i]:
            l.append(i)
    return l
            
    