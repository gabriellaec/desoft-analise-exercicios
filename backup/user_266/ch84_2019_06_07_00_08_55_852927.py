def inverte_dicionario(dicionario):
    flipped = {}
    for k, v in dicionario.items():
        if v not in flipped:
            flipped[v] = [k]
        else:
            flipped[v].append(k)
    return flipped