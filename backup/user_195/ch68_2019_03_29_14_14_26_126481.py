def separa_trios(L):
    i=0
    S=[]
    while i+3<len(L):
        a=L[i:i+3]
        S.append(a)
        i+=3
    if len(L)-i==2:
        S.append(L[i:i+2])
    elif len(L)-i==1:
        S.append(L[i])
    return S