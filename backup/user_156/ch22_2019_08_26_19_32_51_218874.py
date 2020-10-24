def eh_bissexto (x):
    if x%4:
        return True
    elif x%400:
        return True
    else:
        return False