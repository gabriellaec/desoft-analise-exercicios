def eh_bissexto(ano):
    if ano%4==0 or ano != 100 or ano != 1:
        return True
    else:
        return False