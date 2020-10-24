def eh_bissexto(ano):
    a = ano
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        return True
    else:
        return False
    