def soma_impares(lista):
    i=0
    a=0
    while i<len(lista):
        if lista[i]%2!=0:
            a+=lista[i]
        i+=1
    return a
        