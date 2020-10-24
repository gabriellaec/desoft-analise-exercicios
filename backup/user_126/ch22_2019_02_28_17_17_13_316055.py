def eh_bissexto(ano):
    if ano < 4:
        return False
    if ano%4==0 and ano != 100 and ano != 200:
        return True
    else:
        return False