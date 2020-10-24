def soma_impares(lista):
    soma = 0
    for impares in lista:
        if impares % 2 != 0:
            soma += impares
    return soma