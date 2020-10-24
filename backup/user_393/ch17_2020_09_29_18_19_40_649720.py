def eh_bissexto(x):
    if x%4 == 0:
        return True
    elif x%100 != 0:
        if x%400 == 0:
            return True
        else:
            return False
    else:
        return False
        
 