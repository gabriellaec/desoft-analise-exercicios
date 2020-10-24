def soma_impares(lista):
    soma_impares = 0
    i = 0
    while i < len(lista):
        if lista[i]%2 != 0:
            soma_impares = soma_impares + lista[i]
        i+=1
    return soma_impares