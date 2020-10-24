def eh_primo (num):
   #ver se ele é zero ou um e já eliminar
    if num == 0 or num == 1:
        return False
    elif num == 2:
        return True
    else:
        divisor = 2
        primo = True
        while(divisor < num):
            if(num%divisor == 0):
                return False  
                divisor = divisor + 1
            else:
                return False
    
   