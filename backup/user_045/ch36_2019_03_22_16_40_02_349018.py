def eh_primo(n):
    primo=True
    i=2
    if n==1 or n==0:
        primo=false
    while i<n:
        if n%i==0:
            primo=false
        i+=1
    return primo