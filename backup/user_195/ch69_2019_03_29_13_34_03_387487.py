def junta_listas(L):
    i=0
    S=[]
    while i<len(L):
        j=0
        while j<len(L[i]):
            S.append(L[i][j])
            j+=1
        i+=1
    return S