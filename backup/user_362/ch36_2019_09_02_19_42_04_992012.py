def eh_primo(numero):
    if numero == 2:
        return True
    elif numero < 2:
        return False
    #if numero % 2 != 0:
        #return True
    n = 3
    while n < numero:
        if numero % n == 0:
            return False
        n += 2