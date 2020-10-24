def eh_bissexto(ano):
    if ano == 1:
        return True
    if ano%4==0 or ano != 100:
        return True
    else:
        return False