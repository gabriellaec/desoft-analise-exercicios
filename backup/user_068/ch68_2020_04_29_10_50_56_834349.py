def separa_trios(listanomes):
    listatrios = []
    i = 0
    while i < len(listanomes):
        listatrios.append(listanomes[i:i+3])
        i += 3
    return listatrios
                                   
    