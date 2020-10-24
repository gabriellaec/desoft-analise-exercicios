def separa_trios(listanomes):
    listatrios = []
    for i in listanomes:
        listatrios.append(",".join([listanomes[i], listanomes[i+1], listanomes[i+2]]))
    return listatrios
                                   
    