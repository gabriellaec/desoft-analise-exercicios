def eh_bissexto(ano):
    y = ano %4
    x = ano %100
    z = ano %400
    w = 1
    if ano == w:
        return False
    if y == 0:
        return True
    elif x == 0:
        if z == 0:
            return True 
        else:
            return False 