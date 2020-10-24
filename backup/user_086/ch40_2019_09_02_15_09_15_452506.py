def fatorial(n):
    fatorial=1
    #n-1*n-2*n-3*...*n-n
    while fatorial<n:
        fatorial=n-fatorial
        fatorial+=1
    fatorialfinal=fatorial*n
    return fatorialfinal
        