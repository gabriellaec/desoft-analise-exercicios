    if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        if n %2 == 0:
            return False
        else:
            d = 3
            while d < n:
                if n % d == 0:
                    return False
                elif:
                    d += 2
            return True
