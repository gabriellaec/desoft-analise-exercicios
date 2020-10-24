def eh_bissexto(ano):
    a = ano
    if a % 4 == 0 or a % 400 == 0 or a == 1 and not a % 100 == 0:
        return 'true'
    else:
        return 'false'
    
    