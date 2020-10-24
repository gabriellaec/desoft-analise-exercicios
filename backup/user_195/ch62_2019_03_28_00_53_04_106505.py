def filtra_positivos(L):
    i=0
    S=[]
    while i<len(L):
        if L[i]=>0:
            S.append(L[i])
        i+=1
    return S