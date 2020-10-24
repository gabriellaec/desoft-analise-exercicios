def separa_trios(l):
    newl = []
    for i in range(2,len(l),3):
        newl.append([l[i-2],l[i-1],l[i]])
    return newl
        