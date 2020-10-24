def soma_impares(lista):
    l=[]
    i=0
    while i<len(lista):
        if  lista[i]%2 !=0:
            l.append(lista[i])
        i+=1
    s=0
    for e in l:
        s+=e
    return s