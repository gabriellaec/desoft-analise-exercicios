def estritamente_crescente(L):
    i=1
    maior=L[0]
    S=[maior]
    while i<len(L):
        if L[i]>maior:
            maior=L[i]
            S.append(L[i+1])
        i+=1
    return S