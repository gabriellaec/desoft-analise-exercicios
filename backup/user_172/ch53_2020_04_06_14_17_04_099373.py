def soma_impares (lista):
    for i in lista:
        if i%2 != 0:
            soma = soma + i
    return soma