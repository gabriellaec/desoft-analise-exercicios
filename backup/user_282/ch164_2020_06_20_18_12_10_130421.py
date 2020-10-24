def traduz(lista, dicionario):
    traducao = list()
    for i in lista:
        for x, y in dicionario.items():
            if i == x:
                traducao.append(y)
    return traducao