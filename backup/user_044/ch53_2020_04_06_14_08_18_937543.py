def soma_impares(lista):
    soma=0
    x=len(lista)
    for i in range(lista):
        if (lista[i]%2)!=0:
            soma+=lista[i]
    return soma
            