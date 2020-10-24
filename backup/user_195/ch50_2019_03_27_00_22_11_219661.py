def numero_no_indice(L):
    i=0
    S=[]
    while i<len(L):
        if L[i]==i:
            S.append(L[i])
        i+=1
    return S