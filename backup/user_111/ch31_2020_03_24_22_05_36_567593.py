def eh_primo(numero):
    n=2
    if numero==0 or 1:
        return False
    while n<=numero:
        if numero%2 != 0:
            d=3
            while d<numero:
                if numero%d==0:
                    return False
                d+=2
            else:
                return True
        else:
            return False