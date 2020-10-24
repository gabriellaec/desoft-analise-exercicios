def estritamente_crescente(L):
    i=0
    S=[L[0]]
    while i<len(L):
        if L[i+1]>L[i]:
            S.append(L[i+1])
        i+=1
    return S