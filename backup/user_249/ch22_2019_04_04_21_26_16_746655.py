def eh_bissexto(n):
    if n % 4==0 and n % 100!=0 and n % 400==0:
        True
    else:
        False