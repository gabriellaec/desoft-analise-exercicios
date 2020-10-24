def eh_bissexto(x):
    if x==100:
        return False
    elif x==400:
        return False
    elif x%4==0:
        return True
    elif x%400==0:
        return True
    elif x%100==0:
        return False
    else:
        return False
    
  