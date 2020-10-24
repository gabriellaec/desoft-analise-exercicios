def eh_primo(n):
    i=2
    j=0
    if n==0 or n==1:
        return False
    elif n==2:
        return True
    while i<=n:
        if n%i==0:
            return False
        else:
            return True
 