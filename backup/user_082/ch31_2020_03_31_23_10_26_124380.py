def eh_primo(numero):
    i=0
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    if numero % 2 == 0:
        return False
    while (i + 3) < numero:
        if numero % i == 0:
            return False
        i+=2
    else:
        return True