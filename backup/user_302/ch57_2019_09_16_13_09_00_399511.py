def soma_impares(lista):
    lista = [1,2,3,4,5,6,7,8]
    i = 0
    soma = 0
    while i < len(lista):
        num = lista[i] % 20
        if num != 0:
            soma += lista [i]
        i += 1
    return soma
