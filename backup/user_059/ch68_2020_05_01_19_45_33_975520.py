def separa_trios(l):
    noval = [] 
    i = 0
    while i<len(l):
        noval.append(l[i:i+3])
        i+=3
    return noval
    