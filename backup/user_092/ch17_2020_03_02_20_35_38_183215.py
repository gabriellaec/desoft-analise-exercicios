def eh_bissexto(x):
    y = x%4
    if y == 0:
        return True
    elif x%400:
        return True
    elif x/100:
        if x%100==0:
            return False
        else:
            True
    else:
        return False
    