def separa_trios(nomes):
    listan=[]
    for i in range(len(nomes)):
        a=nomes[i:i+3]
        listan.append(a)
    return listan