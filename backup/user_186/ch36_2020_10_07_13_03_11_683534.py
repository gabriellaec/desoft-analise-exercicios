def fatorial(n):
    fatorial=n
    i=1
    while (n-i)>1:
        fatorial=fatorial(-i)
        i+=1
        return fatorial