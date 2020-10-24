def eh_primo(n):
    primo=True
    if n<=1:
        primo=False
    for e in range(2,n):
        if n%e==0 e!=n:
        	primo=False
    return primo