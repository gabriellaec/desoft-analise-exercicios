import math

def calcula_gaussiana(a,b,c):
    p1=(1/(c*math.pow((2*math.pi),(1/2))))
    p2=((-0.5)*((a-b)/c)**2)
    r=math.pow(p1,p2)
    return r 
x=5
y=1
z=4
print(calcula_gaussiana(x,y,z))
   
 