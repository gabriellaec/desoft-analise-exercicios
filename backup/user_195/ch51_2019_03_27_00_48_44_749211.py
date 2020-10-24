def estritamente_crescente(L):
    i=1
    maior=L[0]
    S=[maior]
    while i<len(L)-1:
        if L[i]>maior:
            maior=L[i]
            S.append(L[i])
        i+=1
    return S