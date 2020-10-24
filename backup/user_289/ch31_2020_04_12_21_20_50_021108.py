def eh_primo(numero):
    primo = False
    if numero %2 == 0 and numero != 2:
        n = 1
        while n < numero:
            if numero % n != 0:
                primo = True
            n += 1
    elif numero == 2:
        primo = True
    return primo