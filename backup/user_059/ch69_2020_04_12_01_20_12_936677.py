def junta_listas(l):
    noval = [] 
    i = 0
    while i<len(l):
        j = 0
        while j<len(l[i]):
            noval.append(l[i][j])
            j+=1
        i+=1
    return noval