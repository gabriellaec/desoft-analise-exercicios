def soma_impares (lista):
    i = 0
    soma = 0
    while i < len(lista):
        if lista[i]%2 == 1:
            soma = soma + lista[i]
            i = i + 1
        else:
            i = i + 1
    return soma