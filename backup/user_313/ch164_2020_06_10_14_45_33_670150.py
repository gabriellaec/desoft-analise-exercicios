traduzido = list()
def traduz(l1):
    for i in l1:
        tradução = eng2port[i]
        traduzido.append(tradução)

    return traduzido