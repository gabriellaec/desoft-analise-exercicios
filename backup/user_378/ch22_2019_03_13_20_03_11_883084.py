def eh_bissexto(a):
    if a%400==0:  
       return True
    if a%100==0:
       return True
    elif a%4==0:
       return True
    else:
        return False
