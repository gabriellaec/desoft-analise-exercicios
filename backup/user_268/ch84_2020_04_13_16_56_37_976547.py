def inverte_dicionario(dc):
    chav = dc.keys()
    vlr = dc.values()
    new = {}
    L = []
    L2 = []
    for i in vlr:
        if i not in new:
            for j in chav:
                if dc[j] == i:
                    L.append(j)
            new[i] = L
    return new
            
            