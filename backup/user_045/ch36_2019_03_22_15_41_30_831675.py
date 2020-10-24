def eh_primo(n):
    primo=False
    i=2
    while i<n:
        if n%i!=0:
            primo=True
        i+=1
    return primo