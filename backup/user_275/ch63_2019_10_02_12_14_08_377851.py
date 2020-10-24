def pos_arroba(E):
    i=0
    n=len(E)
    while i<n:
        if E[i] == '@':
            resultado= i
        i+=1
    return resultado