def separa_trios(nomes):
    new = []
    for i in range(0, len(nomes)):
        new.append(nomes[i:i+3])
    return new
        