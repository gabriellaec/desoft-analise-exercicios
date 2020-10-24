def soma_impares(lista):
    soma = 0
    i=1
    while(len(lista)-1):
        if lista[i]%2!=0:
            soma+=lista[i]
        i+=2
    return soma