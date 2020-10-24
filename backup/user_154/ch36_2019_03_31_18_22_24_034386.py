def eh_primo(n):
    if n < 2:
        return False
    test = 2
    while(test < n):
        if ((n % test) == 0):
            return False
        test = test + 1
    return True