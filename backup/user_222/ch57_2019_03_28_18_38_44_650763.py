def soma_impares(numeros):
    i=0
    k=0
    s=0
    while i<len(lista):
        if lista[i]%2==1:
            k=lista[i]
        s+=k
    return s