def soma_valores(lista): 
    soma = 0 
    i = 0
    while i < len(lista):
        soma = lista[i] + soma
        i = i + 1
    return soma
