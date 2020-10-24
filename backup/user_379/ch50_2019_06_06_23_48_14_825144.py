def numero_no_indicie(lista):
    l=[]
    for i in range(len(lista)):
        if i==lista[i]:
            l.append(i)
    return l
            
    