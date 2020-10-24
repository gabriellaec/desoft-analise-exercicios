def eh_bissexto(i):
    if (i%4==0 and i%100==0) or (i%400==0):
        return True
    else:
        return False