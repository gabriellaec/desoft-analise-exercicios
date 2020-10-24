def eh_primo(numero):
    primo = False
    if numero != 0 and 1:
        if numero % 2 != 0:
            for n in range (3, numero):
                if numero % n != 0:
                    primo = True
    elif numero == 2:
        primo = True
    else:
        primo = False
    return primo