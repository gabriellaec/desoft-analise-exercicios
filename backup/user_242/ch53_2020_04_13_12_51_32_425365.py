def soma_impares(lista):
    soma = 0
    i=1
    for i in range(len(lista)-1):
        if lista[i]%2!=0:
            soma+=lista[i]
            i+=2
    return soma