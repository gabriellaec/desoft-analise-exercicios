def eh_primo(numero):
    i=2
    if numero <= 1:
        return False
    if numero <=3:
        return True
    if numero % 2 == 0:
        return False
    while (i + 3) < numero:
        if numero % i == 0:
            return False
        i+=2
    else:
        return True