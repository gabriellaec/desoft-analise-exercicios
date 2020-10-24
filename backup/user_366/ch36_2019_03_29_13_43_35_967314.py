def eh_primo(n):
    if (n > 2 and n % 2 == 0) or n < 2:
        return False
    elif n == 2 or n ==3:
        return True
    else:
        intervalo = range(3, n, 2)
        for e in intervalo:
            if n % e == 0:
                return False

        return True