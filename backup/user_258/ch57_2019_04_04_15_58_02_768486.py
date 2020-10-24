def soma_impares(lista):
    soma=0
    i=lista[len(lista)-1]
    while i>=1:
        if lista[i]%2!=0:
            soma+=lista[i]
        i-=1
    return soma
            