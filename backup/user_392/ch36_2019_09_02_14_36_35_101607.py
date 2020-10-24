def eh_primo(x):
    i = 3
    if x == 1 or x == 0:
        return False
    if x == 2:
        return True
    if x%2 == 0:
        return False
    while i < x:
        if x%i == 0:
            return False
        i+=2
    return True