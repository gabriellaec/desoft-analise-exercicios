def traduz(lista, dicionario):
    traducao = []
    i = 0
    while i < len(lista):
        for ing, port in dicionario.items():
            if lista[i] == ing:
                traducao.append(dicionario[ing])
        i += 1
    return traducao