def conta_a(n):
    tam=len(n)
    i=0
    c=0
    while i < tam:
        if n[i] == "a":
            c=c+1
        i=i+1
    return c