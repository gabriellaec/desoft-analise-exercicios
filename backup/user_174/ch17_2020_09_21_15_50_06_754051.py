def eh_bissexto(ano):
    if ano%4==0 and ano%100 !=0:
        return True
    else:
        if ano%400==0 and ano%100 !=0:
            return True
        else:
            if ano%100==0:
                return False
  
       
    
    