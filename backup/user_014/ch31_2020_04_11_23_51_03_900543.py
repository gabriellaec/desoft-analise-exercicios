def eh_primo (n):
    d = 2
    t = 3
    if n == 0 or n == 1:
        return False
    elif n == d or n == 3:
        return True
    else:
        while n % d != 0 and d < n:
            d += 1
        if n % d == 0:
            return False
        else:
            return True
                
            