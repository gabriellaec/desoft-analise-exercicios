def interseccao_chaves(d1,d2):
    chaves=[]
    d1_keys=d1.keys()
    for e in d1_keys:
        if e in d2.keys():
            chaves.append(e)
    return chaves
    
