def eh_bissexto(n):
    if n%400 == 0:
        return True
    elif n%100 == 0:
        return False
    elif n%4 == 0:
        return True
    else:
        return False