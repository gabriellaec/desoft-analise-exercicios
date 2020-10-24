def encontra_maximo(l):
    l1 = [] 
    i = 0
    while i<len(l):
        l1.append(l[i][0])
        l1.append(l[i][1])
        l1.append(l[i][2])
        i+=1
    j = max(l1)
    if j>=0:
        return j
    else:
        return (j*(-1))