def interseccao_valores(dicionario1,dicionario2):
    lista_de_valores = []
    for valor in dicionario1:
        if dicionario1[valor] == dicionario2[valor]:
            lista_de_valores.append(valor)
    return lista