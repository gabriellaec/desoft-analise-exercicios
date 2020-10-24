def eh_bissexto(n):
    if n % 4 and n % 100 and n % 400==0:
        return True
    else:
        return False