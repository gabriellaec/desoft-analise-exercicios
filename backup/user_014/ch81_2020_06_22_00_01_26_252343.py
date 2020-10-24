def interseccao_valores(dicionario_1, dicionario_2):
    lista_valores_1 = []
    lista_valores_2 = []
    for valores_1 in dicionario_1.values():
        lista_valores_1.append(valores_1)
    for valores_2 in dicionario_2.values():
        lista_valores_2.append(valores_2)
    lista_final = []
    i = 0
    while i < len(lista_valores_1):
        if lista_valores_2[i] in lista_valores_1:
            lista_final.append(lista_valores_2[i])
        i += 1
    return lista_final