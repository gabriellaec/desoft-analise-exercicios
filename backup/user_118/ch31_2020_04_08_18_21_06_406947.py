def eh_primo(numero):
    if numero != 0 and numero != 1:
        if numero > 3:
            for i in range(2, numero):
                if numero % i == 0:
                    return False
        return True
    return False
