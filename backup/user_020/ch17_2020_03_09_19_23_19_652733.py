def eh_bissexto(n):
    if n % 4 == 0 and n % 100 != 0:
        return True
        if n % 100 == 0 and n % 400 == 0:
            return True
    elif n % 400 != 0:
        return False
    else:
        return False