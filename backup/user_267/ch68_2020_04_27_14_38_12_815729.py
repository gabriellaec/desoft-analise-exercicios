def separa_trios(nomes):
    new = []
    for i in range(0, len(nomes)):
        new.append([nomes[i], nomes[i+1], nomes[i+2]])
    return new
        