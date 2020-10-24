def soma_impares(lista):
    l=[]
    i=0
    while i<len(lista):
        if  lista[i]%2 !=0:
            l.append(lista[i])
    s=0
    for e in l:
        s+=e
    return s