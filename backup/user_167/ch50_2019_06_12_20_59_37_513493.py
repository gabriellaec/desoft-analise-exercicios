def numero_no_indice (lista):
    l=[]
    i=0
    while i < len(lista):
        if i==lista[i]:
            l.append(i)
        i+=1
    return l
            