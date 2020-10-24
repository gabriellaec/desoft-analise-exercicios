def eh_primo(numero):
    if numero == 0 or numero == 1:
        return False
    if numero == 2 or numero == 3:
        return True
    i=3
    while i < numero:
        if numero % i == 0:
            return False
        i=i+1 
    else:
        return True
        