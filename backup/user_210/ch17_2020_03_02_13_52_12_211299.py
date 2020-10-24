def eh_bissexto(ano):
    if (ano%4==0) and (ano%100!=0):
        if ano%400==0:
            return True
    elif ano%4!=0:
        return False