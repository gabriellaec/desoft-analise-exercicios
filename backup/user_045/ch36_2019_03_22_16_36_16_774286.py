def eh_primo(n):
    primo=True
    i=2
    while i<n:
        if n%i==0:
            primo=false
        i+=1
    return primo