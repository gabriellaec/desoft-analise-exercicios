def eh_bissexto(n):
    if n %4==0 and n %100!=0:
        return True
    if  n %4==0 and n %400==0:
        return True
    if n==0:
        return True
    else:
        return False
    
a=eh_bissexto(400)
print(a)