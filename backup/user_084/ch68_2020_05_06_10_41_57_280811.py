def separa_trios(x):
    l=[]
    i=0
    while i<len(x):
        l.append(x[i:i+3])
        i+=3
    return l
                 