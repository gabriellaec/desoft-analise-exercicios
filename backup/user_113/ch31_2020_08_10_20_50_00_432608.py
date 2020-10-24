def eh_primo(n):
    resto = n/2
    #if resto == 0:
        #return False
    x=1
    while x<=n:
        sao = n/x
        if sao == 0:
            return False
        x += 2
    else:
        return True