def conta_a(texto):
    c=0
    i=0
    n=len(texto)
    
    while i<n:
        if texto[i] == 'a':
            c+=1
        i+=1
    return c
