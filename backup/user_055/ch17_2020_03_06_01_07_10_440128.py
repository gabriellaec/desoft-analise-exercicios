def eh_bissexto(ano):
    if ano % 4 == 0 or ano % 400 == 0:
        return True
    if ano % 4 == 0 and ano % 100 == 0 and ano % 400 != 0:
        return False
    else:
        return False
    
    

