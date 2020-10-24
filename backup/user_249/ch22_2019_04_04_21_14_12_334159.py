def eh_bissexto(n):
    if n % 4==0:
        True
    elif n % 100==0:
        True
    elif n % 400==0:
        True
    else:
        False
return (eh_bissexto(n))