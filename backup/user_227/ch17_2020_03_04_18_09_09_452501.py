import math
def eh_bissexto(a):
    if  a%400==0:
        return(True)
    else:
        if a%100==0:
            return(False)
        elif a%4==0 or a==1:
            return(True)
        else:
            return(False)
        
       