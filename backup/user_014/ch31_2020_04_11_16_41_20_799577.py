def eh_primo(n):
    if n == 0 or n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(3, n, 2):
            if n % 2 == 0:
                return False
            elif n % i == 0:
                return True