def soma_impares (lista):
    i= 0
    soma= 0
    while i<len(lista):
        if lista[i] % 2 == 0:
            i= i + 1
        else:
            soma = soma + lista[i]
            i= i + 1
    return soma