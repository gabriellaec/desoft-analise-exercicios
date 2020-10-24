def eh_bissexto(ano):
    if ano%4==0:
        if ano%100==0 and ano%400!=0:
            return False
        return True
    else:
        return False
       