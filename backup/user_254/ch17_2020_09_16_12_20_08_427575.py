def eh_bissexto(ano):
    if int(ano/4) == ano/4:
        if ano == 100:
           return False 
        else:
            return True
    else:
        return False