def fatorial(n):
    fact=1
    termo=0
    i=0
    while i < n:
        termo = n-i
        fact= fact*termo
        i+=1
    return fact
    