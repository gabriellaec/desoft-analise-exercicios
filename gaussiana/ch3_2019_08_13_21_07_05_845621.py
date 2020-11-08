import math
def calcula_gaussiana(w,x,z):
    y=1/(z(2*math.pi)**(1/2))*math.exp(-0.5*((w-x)/z)**2)
    return y
a=100000
b=100000
c=0.1
d=calcula_gaussiana(a,b,c)
print(d)