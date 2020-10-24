def eh_primo(n):
    i=1
    j=0
    if n==0 or n==1:
        return False
    elif n==2:
        return True
    while i<=n:
        if n%2==0:
            return False
        elif n%i==0:
            return False
        else:
            return True
    i+=2