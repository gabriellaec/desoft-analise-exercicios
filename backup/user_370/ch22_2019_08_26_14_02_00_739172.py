def eh_bissexto (n):
    if n%400==0:
        return True 
    elif n%4==0:
        return True 
    elif n%100:
        return False 