def encontra_cateto (a,b):
    c=((x**2)-(y**2))**(1/2)
    return c 
x=int(input('hipotenusa: '))
y=int(input('cateto1: '))
k=encontra_cateto (x,y)
print (k)