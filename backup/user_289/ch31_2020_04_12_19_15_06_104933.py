def eh_primo(numero):
    primo = False
    if numero != 0 and numero != 1 and numero != 2:
        n = 2
        while n < numero:
            n += 1
            if numero % n != 0:
                primo = True
    elif numero == 2:
        primo = True
    return primo