
def eh_bissexto(a):
    if a%4==0:
        if a%100!=0:
            return True
        elif a%100==0:
            if a%400:
                return True    
            else: 
                return False
    else:
        return False
