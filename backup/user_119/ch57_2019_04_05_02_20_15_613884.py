def soma_impares(lista):
    soma=0
    i=0
    e=0
    while i<len(lista):
        if lista[i]%2==1:
            lista[i]=e
            soma+=e
            i+=i
    return soma