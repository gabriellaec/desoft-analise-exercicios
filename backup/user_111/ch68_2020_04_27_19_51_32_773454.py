def separa_trios(nomes):
    listan=[]
    for i in range(0,len(nomes),3):
        a=nomes[i:i+3]
        listan.append(a)
    return listan