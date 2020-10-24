def pos_arroba(E):
    i=0
    n=len(E)
    while i<n:
        if E[i] == '@':
            resultado= i+1
        i+=1
    return resultado