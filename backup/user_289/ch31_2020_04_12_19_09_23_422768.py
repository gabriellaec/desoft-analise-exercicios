def eh_primo(numero):
    primo = False
    if numero != 0 and numero != 1 and numero != 2:
        if numero % 2 != 0:
            for n in range (2, numero):
                if numero % n != 0:
                    primo = True
    elif numero == 2:
        primo = True
    else:
        primo = False
    return primo