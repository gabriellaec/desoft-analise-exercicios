def separa_trios(nomes):
    trios = []
    i = 0
    while i < len(nomes):
        t = nomes[i::3]
        trios.append(t)
        i += 1
    return trios
       