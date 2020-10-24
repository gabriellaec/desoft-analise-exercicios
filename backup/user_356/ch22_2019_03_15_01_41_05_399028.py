def eh_bissexto(n):
    if n %4==0 and n %100!=0:
        return True
    else:
        return False
        
a=eh_bissexto(2012)

print(a)