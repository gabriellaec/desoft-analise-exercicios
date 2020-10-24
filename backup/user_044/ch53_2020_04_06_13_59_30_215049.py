def soma_impares(lista):
    soma=0
    for i in lista:
        if (lista[i]%2)!=0:
            soma+=lista[i]
    return soma
            