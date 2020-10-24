def soma_impares(lista):
    soma = 0
    for i in lista:
        if i%2 != 2:
            soma += i
    return soma

numeros = [2, 5, 89, 413, 3, 10, 96, 77, 57, 197, 32]
print(soma_impares(numeros))