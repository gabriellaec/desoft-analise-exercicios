def encontra_maximo(l):
    l1 = [] 
    i = 0
    while i<len(l):
        l1.append(l[i][0])
        l1.append(l[i][1])
        l1.append(l[i][2])
        i+=1
    j = 0
    norma = 0
    while j<len(l1):
        if l1[j]>l1[j-1]:
            norma = l1[j]
    return j