def eh_primo(numero):
    if numero != 0 and numero != 1:
        if numero > 3:
            while 2 <= i <= numero:
                if numero % i == 0:
                    return False
        return True
    return False
