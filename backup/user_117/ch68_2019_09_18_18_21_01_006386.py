def separa_trios(nomes):
    trios = []
    i = 0
    while i < len(nomes[0:3]):
        trios.append(nomes[i])
        del nomes[i]
    return trios