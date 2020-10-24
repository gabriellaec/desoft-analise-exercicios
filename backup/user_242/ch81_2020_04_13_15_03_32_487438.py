def interseccao_valores(dicionario1,dicionario2):
    lista_de_valores = []
    valores1 = dicionario1.values()
    valores2 = dicionario2.values()
    for valor in valores1 :
        if valor in valores2:
            lista_de_valores.append(valor)
    return lista_de_valores