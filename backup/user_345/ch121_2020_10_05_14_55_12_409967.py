def subtracao_de_listas(lista1, lista2):
    resultado = []
    i = 0
    while i <= len(lista1):
        if i not in lista2:
            resultado.append(lista1[i])
    return resutado
        