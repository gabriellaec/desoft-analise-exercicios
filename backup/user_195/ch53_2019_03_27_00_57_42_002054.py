def inverte_lista(L):
    i=1
    S=[]
    while i<=len(L):
        S.append(L[len(L)-i])
        i+=1
    return S