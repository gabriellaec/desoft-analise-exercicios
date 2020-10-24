def separa_trios(nomes):
    trios = []
    i = 0
    while i < len(nomes):
        t = nomes[i:i+3]
        trios.append(t)
        i += 3
    return trios
       