def eh_primo(n):
    primo=True
    i=2
    if n<=1:
        primo=False
    while i<n:
        if n%i==0:
            primo=False
        i+=1
    return primo
def verifica_primos(n):
    d={}
    for e in n:
        d[e]=teste(e)
    return d
