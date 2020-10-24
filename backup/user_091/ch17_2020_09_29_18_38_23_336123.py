def eh_bissexto(ano):
    if ano%4==0:
        if ano%100==0:
            return False
        else:
            return True
    elif ano%100==0:
        return False
    else:
        return False