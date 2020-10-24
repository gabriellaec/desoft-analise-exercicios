def eh_bissesto(ano):
    if ano%4==0:
        return True
    elif ano%400==0:
        return True
    elif ano%100!=0:
        return True
    else:
        return False