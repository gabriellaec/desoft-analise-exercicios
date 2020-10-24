def eh_primo(numero):
    n=2
    if numero==0:
        return ("0 não é primo")
    while n<=numero:
        if numero%2 != 0:
            d=3
            while d<numero:
                if numero%d==0:
                    return ("Não é primo")
                d+=2
            else:
                return ("É primo")
        else:
            return ("Não é primo")