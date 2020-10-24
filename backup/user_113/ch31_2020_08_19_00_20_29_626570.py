def eh_primo(n):
    if n==0 or n==1:
        return False
    elif n==2:
        return True
    x=3
    while x<=n:
        primos = n/2
        if primos == 0:
            return False
            x += 2
        else:
            return True
    