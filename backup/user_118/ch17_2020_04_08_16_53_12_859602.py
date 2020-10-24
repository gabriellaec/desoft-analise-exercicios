def eh_bissexto(ano):
    if ano%4 and not ano%100:
        return True 
    elif ano%400:
        return True
    else:
        return False