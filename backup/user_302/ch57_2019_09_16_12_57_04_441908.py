def soma_impares(lista):
    lista = []
    i = 0
    soma = 0
    while i < len(lista):
        num = lista[i] % 2
        if num != 0:
            soma += lista [i]
        i += 1
    return soma
print ("A soma dos termos ímpares da lista é {0}".format(soma))