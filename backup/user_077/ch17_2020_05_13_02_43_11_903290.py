def eh_bissexto(x):
    if x%400==0:
        return True
    elif x%100==0 or x%4!=0:
        return False
    else:
        return True
    