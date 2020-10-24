def eh_bissexto(ano):
    if ano%400==0:
        return True 
    elif ano%100:
        return False
    elif ano%4:
        return True
    else:
        return False