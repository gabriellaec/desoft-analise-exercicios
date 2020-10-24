def eh_bissexto(n):
    if n % 4:
        True
    elif n % 100:
        True
    elif n % 400:
        True 
    else:
        False