def eh_bissexto(x): 
    if x >= 400 and x%400 == 0 and x%4 == 0 and x%100 != 0 or x%4 == 0 and x%100 != 0:
        return True
    else:
        return False