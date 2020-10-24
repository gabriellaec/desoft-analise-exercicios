def eh_bissexto(x):
    if x%4 == 0:
        if x%100 == 0:
            if x%400 == 0:
                return True
            else:
                return False
           
         
        else:
            return True
    
    else:
        return False