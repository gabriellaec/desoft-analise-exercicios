def junta_listas (lista):
    lista2 = []
    i = 0
    soma = 0
    while i < len(lista):
        lista2.append(lista[i])
        soma += lista2
        i += 1
    return soma
        