def separa_trios(nomes):
    d = list()
    for i in nomes:
        d.append(list(nomes[0:3:3]))
    return d