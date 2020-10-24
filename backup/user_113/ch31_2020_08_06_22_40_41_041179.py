def eh_primo(n):
    resto = n/2
    if resto==0:
        return False
    x=1
    while x<=n:
        resto2 = n/x
        if resto2 == 0:
            return False
        else:
            x += 2