def eh_primo(numero):
    if numero%2 == 0 or numero == 1 or numero == 0:
        return False
    i = 3
    while i < numero:
        if numero%i == 0:
            return False
            break
        else:
            return True