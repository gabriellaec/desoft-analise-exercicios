def eh_bissexto(n):
    if n % 4==0:
        return True
    elif n % 100==0:
        return True
    elif n % 400==0:
        return true
    else:
        return False