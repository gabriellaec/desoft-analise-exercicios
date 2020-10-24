def separa_trios(nomes):
    trios=[]
    i=0
    while i < len(nomes):
        trios.append(nomes[i:i+3])
        i+=3
    return trios