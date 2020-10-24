def eh_primo(numero):
    i=3
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    while (i) < numero:
        if numero % i == 0 or numero == i:
            return False
        i+=1
        else:
            return True