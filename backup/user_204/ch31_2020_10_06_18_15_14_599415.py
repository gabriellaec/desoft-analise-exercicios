def eh_primo(numero):
    if numero < 0:
        return False
    elif numero == 0 or numero == 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False