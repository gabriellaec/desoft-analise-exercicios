def separa_trios(nomes):
    trios=[]
    for i in range(0,len(nomes),3):
        trios.append(nomes[i:i+3])
    print(trios)
    return trios