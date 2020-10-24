def eh_bissexto(a):
    if a%400 == 0:
        return True
    if a%4 == 0 and a%100!=0:
        return True
    return False
   

