def eh_bissexto(ano):
    
    if ano%10 == 0:
        return False
    if ano%4 == 0:
        return True
    else:
        return False 