def soma_impares(lista):
    soma=0
    i=0
    while i < len(lista):
        if lista[i] % 2 != 0:
            soma+=lista[i]
        i+=1
    return soma
numeros=[0,1,2,3,4,5]
print(soma_impares(numeros))