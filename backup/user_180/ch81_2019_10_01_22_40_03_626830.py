def interseccao_valores(dicionario1, dicionario2):
    lista_valores_iterseccao = []
    lista_valores1 = list(dicionario1.values())
    lista_valores2 = list(dicionario2.values())
    for valores in lista_valores1:
        if valores in lista_valores2:
            lista_valores_iterseccao.append(valores)
    return lista_valores_iterseccao