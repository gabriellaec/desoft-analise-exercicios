traduzido = list()
def traduz(l1, eng2port):
    for i in l1:
        tradução = eng2port[i]
        traduzido.append(tradução)

    return traduzido