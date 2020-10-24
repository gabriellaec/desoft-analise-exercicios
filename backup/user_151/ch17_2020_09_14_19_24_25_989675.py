def eh_bissexto(x):
    a = x % 100
    if a == 0:
        if x % 400 == 0:
            return True
        else:
            return False
    elif x % 4 == 0:
        return True
    else:
        return False
             