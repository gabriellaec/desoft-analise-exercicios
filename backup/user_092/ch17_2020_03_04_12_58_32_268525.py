def eh_bissexto(x):
    if x%4 and x%400:
        return True
    elif x%100:
        return False
    else:
        return False