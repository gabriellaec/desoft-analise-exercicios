def separa_trios(l):
    newl = []
    for i in range(0,len(l),3):
        newl.append(l[i:i+3])
    return newl