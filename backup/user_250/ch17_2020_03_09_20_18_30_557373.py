def eh_bissexto(y):
    if y%400==0:
        return True
    if y%100!=0 and y%4==0:
        return True
    else:
        return False
    