def soma_impares(lista):
    soma = 0
    for i in lista:
        if i%2==1:
            soma += i
    return soma