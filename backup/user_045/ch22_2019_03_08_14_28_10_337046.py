def eh_bissexto(a):
    if a/400==int:
        return 'true'
    elif a/100==int:
        return 'false'
    elif a/4==int:
        return 'true'
    else:
        return 'false'