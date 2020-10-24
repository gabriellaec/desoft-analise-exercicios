def fatorial(n):
    i=1
    fatorial=n*(n-i)
    while (n-i)>1:
        fatorial=fatorial*(n-i)
        i+=1
    return fatorial