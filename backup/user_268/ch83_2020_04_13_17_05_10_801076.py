def inverte_dicionario(dc):
    chav = dc.keys()
    vlr = dc.values()
    new = {}
    L = []
    L2 = []
    for i in chav:
        b = dc[i]
        if b not in new:
            new[b] = i
        else:
            new[b] += i
    return new

    
    