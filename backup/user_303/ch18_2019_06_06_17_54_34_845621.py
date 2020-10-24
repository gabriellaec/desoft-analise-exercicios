import math 
def encontra_cateto(a,n):
    if a>n:
        hipotenusa=a
        cateto1=n 
    if n>a: 
        hipotenusa=n 
        cateto1=a
    cateto2= math.sqrt((hipotenusa**2)-(cateto1**2))
    return cateto2