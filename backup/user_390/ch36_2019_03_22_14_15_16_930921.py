def verifica_primo(n):
    primo=True
    i=2
    while i<n:
        if n%i==0:
            primo=False
        i+=i
    return primo