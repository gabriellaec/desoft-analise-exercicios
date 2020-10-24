def eh_bissexto(z):
    if z%400== 0:
        return True
    elif z%400 != 0 and z%100==0:
        return False
    elif z%4 == 0:
        return True
    else:
        return False

