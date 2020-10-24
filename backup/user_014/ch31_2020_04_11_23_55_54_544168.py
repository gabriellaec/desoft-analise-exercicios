def eh_primo (n):
    d = 2
    if n == 0 or n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        if n % d == 0:
            return False
        while n % d != 0 and d < n:
            d += 1
        if n % d == 0:
            return False
        else:
            return True         