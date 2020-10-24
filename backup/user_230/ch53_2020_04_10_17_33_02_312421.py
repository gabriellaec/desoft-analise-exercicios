def soma_impares(lista):
    if lista==[]:
        return 0
    soma=0
    for i in range(len(lista)):
        if lista[i]%2!=0:
            soma+=lista[i]
    return soma
    