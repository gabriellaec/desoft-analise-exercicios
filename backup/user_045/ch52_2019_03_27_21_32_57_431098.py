def eh_crescente(n):
    i=1
    crescente=True
    while (i-1)<len(n):
        if n[i]<=n[i-1]:
            crescente=False
        i+=1
    return crescente
        