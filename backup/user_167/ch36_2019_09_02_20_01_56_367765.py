def eh_primo (x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        n = 3
        while n < x:
            if x % n == 0:
                return False
            n += 2
        return True
        

