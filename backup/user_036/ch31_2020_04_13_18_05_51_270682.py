def eh_primo(n):
    if n == 0:
        return False
    elif n == 2:
        return True
    elif n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True