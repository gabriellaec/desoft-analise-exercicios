def soma_impares(lista):
    s=0
    i=0
    while i<len(lista):
        if lista[i]%2!=0:
            s+=lista[i]
        i+=1
    return s
