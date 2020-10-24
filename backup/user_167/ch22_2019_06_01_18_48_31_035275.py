def eh_bissexto (x):
    if x % 400==0:
        return true
    elif x% 100==0:
        return false
    elif x% 4==0:
        return true
    else:
        return false
    
        
  