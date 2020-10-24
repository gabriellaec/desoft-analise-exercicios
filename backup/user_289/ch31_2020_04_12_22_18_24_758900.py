def eh_primo(numero):
    if numero %2 != 0 and numero != 2 or 0 or 1:
        n = 3
        while n < numero:
            if numero % n != 0:
                return True
            n += 1
    elif numero == 2:
        return True
    elif numero == 0 or 1:
        return False
    else:
        return False