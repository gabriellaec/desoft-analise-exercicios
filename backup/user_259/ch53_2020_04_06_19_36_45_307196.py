def soma_impares(lista):
    impares = []
    for i in lista:
        if i%2!=0:
            impares.append(i)
    return impares
print(soma_impares([1, 2, 3]))