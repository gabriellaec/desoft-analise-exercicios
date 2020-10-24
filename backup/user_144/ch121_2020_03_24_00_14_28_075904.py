

def subtracao_de_listas(lista1,lista2):
    valores_pos = []
    for i in range(len(lista1)):
        if lista1[i] in lista2[i]:
            valores_pos.append(lista2[i])
    return valores_pos