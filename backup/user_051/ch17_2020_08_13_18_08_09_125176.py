def eh_bissexto(B):
    if (B%4==0) and (B%400==0):
        return True
    else:
        return False
        