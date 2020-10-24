def junta_listas (lista):
    lista2 = []
    soma = []
    i = 0
    x = 0
    while i < len(lista):
        lista2.append(lista[i])
        soma += lista2[x]
        i += 1
        x += 1
    return soma
        