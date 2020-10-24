def traduz(l, dici):
    traduzida = []
    for i in range(len(l)):
        traduzida.append(dici.get(l[i]))
    return traduzida
