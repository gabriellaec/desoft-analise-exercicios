def eh_bissexto(ano):
    bissexto = ano%4
    if bissexto != 0:
        return False
    else:
        return True

eh_bissexto(ano)