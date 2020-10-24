def separa_trios(l):
    newl = []
    for i in range(0,len(l)):
        newl.append([l[i],l[i+1],l[i+2]])
    return newl
        