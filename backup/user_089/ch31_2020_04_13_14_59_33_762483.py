def eh_primo(x):
    i = 3
    if x % 2 == 0 and x != 2 or x == 0 or x == 1:
        return False
    while x > i:
        if x % i == 0:
            return False
        else:
            return True         