import math
def calcula_gaussiana(x,y,z):
    a= (1/z)
    b= (1/(2*math.pi)**0.5)
    c= (math.e**((1-1.05)*(((x-y)/z)**2))
    d= a*b*c    
    return d
        

       
       