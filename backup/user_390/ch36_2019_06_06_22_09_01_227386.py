def eh_primo(n):
    primo=True
    i=2
    while i<n:
        if n%i==0:
            primo=False
        i+=1
    if n<=1:
        return False
    else:
        return primo
 