def eh_primo(n):
    if n==0 or n==1:
        return False
    resto = n/2
    if resto==0:
        return False
    x=1
    while x<=resto:
        primos = resto/x
        if primos == 0:
            return False
        x += 2
    else:
        return True