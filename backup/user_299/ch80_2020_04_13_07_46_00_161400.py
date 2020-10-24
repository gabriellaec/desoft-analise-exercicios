def interseccao_chaves (dici1, dici2):
    listak = []
    for e in dici1:
        for f in dici2:
            if e == f and e not in listak:
                listak.append(e)
    return listak