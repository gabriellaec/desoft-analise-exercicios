def eh_bissexto(x):
    if (x%100)==0 and x%400==0 or x%4==0:
        return True
    else:
        return False