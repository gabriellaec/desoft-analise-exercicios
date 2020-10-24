def eh_bissexto(ano):
    if ano%4==0:
        if ano%100!=0:
            if ano%400==0 or ano%400==4:
                return True
    return False 