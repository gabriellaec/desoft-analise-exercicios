def monta_dicionario(x, y):
    mm = {}
    for i in x:
        for e in y:
            mm[i] = e
            y.remove(e)
            break
    return mm
        