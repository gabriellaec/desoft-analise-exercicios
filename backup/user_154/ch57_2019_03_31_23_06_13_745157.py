def soma_impares(lista):
    soma = 0
    
    for x in lista:
        if x % 2 != 0:
            soma = soma + x
    return soma