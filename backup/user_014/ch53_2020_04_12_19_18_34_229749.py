def soma_impares(lista):
    i = 0
    soma = 0
    while i < len(lista):
        if lista[i] % 2 != 0:
            soma = soma + lista[i]
        else:
            soma = soma
        i += 1
    return soma