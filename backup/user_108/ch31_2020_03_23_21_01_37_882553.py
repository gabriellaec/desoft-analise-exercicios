def eh_primo(n):
    if n < 2:
        return False
    elif n == 2:
        return True

    x = 2
    while x < n:
        if n % x == 0:
            return False
        x += 1
    return True