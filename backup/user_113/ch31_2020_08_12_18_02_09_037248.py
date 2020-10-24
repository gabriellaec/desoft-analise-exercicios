def eh_primo(n):
    resto = n/2
    if n==0 or n==1:
        return False
    x=1
    while x<=n:
        primos = resto/x
        if primos == 0:
            return False
        x += 2
    else:
        return True