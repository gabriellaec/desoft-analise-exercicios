def eh_bissexto(ano):
    if ano % 4 == 0 and ano % 400 ==0:
        return True
    else:
        if ano % 100 == 0 and ano % 400 != 0 and ano ==1:
            return False
    

