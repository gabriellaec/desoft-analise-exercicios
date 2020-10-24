def eh_primo(n):
    if n==0 or n==1:
        return False
    elif n==2:
        return True
    x = 3
    while x < n:
        resto = n/2
        if n%x != 0:
            x += 2
        else:
            return False
    return True