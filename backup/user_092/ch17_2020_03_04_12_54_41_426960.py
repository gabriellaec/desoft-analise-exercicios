def eh_bissexto(x):
    y = x%4
    z = x%400
    a = x%100
    if y == 0:
        return True
    elif z == 0:
        return True
    elif a != 0:
        return True 
    else:
        return False
    