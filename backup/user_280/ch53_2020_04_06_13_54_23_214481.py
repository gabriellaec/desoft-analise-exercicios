def soma_impares(lista):
    soma = 0
    ímpar = True
    for i in range(len(lista)):
        if lista[i]%2 == 0:
            return False
        else:
            soma += lista[i]
            return True
    return soma
            