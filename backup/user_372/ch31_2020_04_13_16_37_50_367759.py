def eh_primo(n):
    i=1    
    while i<=n and n>0:
        if n%2!=0 and n%i!=0:
            primo=True 
        else:
            primo=False
        i+=2
        return primo
        