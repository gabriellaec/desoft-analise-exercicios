def eh_bissexto(ano):
    if ano%400==0 and ano%4==0:
        return True 
    elif ano%100:
        return
    else:
        return False