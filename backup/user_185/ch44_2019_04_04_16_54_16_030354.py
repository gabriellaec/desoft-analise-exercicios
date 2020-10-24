def soma_valores(lista):
    index = 0
    soma = 0
    while index < len(lista):
        soma = lista[index] + soma
        index = index + 1
    return soma
        
        