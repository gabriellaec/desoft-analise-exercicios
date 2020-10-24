def soma_impares(lista):
    soma=0
    for c in lista:
        x=c%2
        if x!=0:
            soma+=c
    return soma