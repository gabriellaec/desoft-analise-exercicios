def eh_bissexto(x):
    y = x%4
    if y == 0:
        return True
    elif x%400:
        return True
    z = x%100
    elif z!=0:
        return True
    else:
        return False
    