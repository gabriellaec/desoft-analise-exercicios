def junta_listas (lista):
    lista2 = []
    i = 0
    soma = 0
    x = 0
    while i < len(lista):
        lista2.append(lista[i])
        i += 1
        soma += lista2[x]
        x += 1
    return soma
        