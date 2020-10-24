def soma_impares(números):
    soma = 0
    i = 0
    while i in len(números):
        if números[i]%2 != 0:
            soma = soma + números[i]
        i = i + 1
        return soma 