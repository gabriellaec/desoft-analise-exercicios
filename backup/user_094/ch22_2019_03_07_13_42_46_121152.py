def eh_bissexto(ano):
    if ano%4==0:
        if ano%100==0:
            return False
        else:
            return True
    elif ano%400==0:
        return True
    else:
        return False