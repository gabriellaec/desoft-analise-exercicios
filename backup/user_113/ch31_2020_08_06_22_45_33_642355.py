def eh_primo(n):
    resto = n/2
    x=1
    while x<=resto:
        sao = resto/x
        if sao == 0:
            return False
        x += 2
    else:
        return True