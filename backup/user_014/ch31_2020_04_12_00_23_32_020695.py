def eh_primo (n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    else:
        if n % 2 == 0:
            return False
        else:
            d = 2
            while n % d != 0 and n <= d:
                d += 1
                if n % d == 0:
                    return False
                else:
                    return True
        return False