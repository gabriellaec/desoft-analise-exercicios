def soma_valores(lista):
    i=0
    s=0
    while i<len(lista):
        s+=lista[i-1]+lista[i]
        i+=1
    return s 