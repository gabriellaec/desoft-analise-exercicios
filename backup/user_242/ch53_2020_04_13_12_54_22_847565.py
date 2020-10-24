def soma_impares(lista):
    soma = 0
    i=0
    while i < len(lista)-1:
        if lista[i]%2!=0:
            soma+=lista[i]
        i+=1
    return soma
