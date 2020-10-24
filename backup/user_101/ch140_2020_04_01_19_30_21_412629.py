def faixa_notas(l):
    l_ruim = []
    l_medio = []
    l_bom = []
    for e in l:
        if e < 5:
            l_ruim.append(e)
        elif 5 <= e <=7:
            l_medio.append(e)
        else:
            l_bom.append(e)
    l_final = [len(l_ruim), len(l_medio), len(l_bom)]
    return l_final