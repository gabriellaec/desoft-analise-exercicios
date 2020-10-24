def eh_bissexto(x):
    if x%4 == 0 and x%100 != 0:
        return True 
    else:
        return False