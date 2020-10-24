def eh_bissexto(x):
    if x%4 and x%400 and x%100:
        return True
    else:
        return False