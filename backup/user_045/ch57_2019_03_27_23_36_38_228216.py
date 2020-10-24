def soma_impares(n):
    i=0
    s=0
    while i<len(n):
        if n[i]%2!=0:
            s=s+n[i]
        i+=1
    return s