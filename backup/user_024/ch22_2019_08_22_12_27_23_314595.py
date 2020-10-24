def eh_bissexto(ano):
    if int(ano/400)/(ano/400)==1:
        return True
    elif int(ano/100)/(ano/100) == 1:
        return False
    elif int(ano/4)/(ano/4) == 1:
        return True
    else:
        return False
    
    