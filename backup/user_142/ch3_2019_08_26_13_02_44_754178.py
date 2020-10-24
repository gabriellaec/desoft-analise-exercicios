import math 
def calculo_gaussiana (x,u,o):
    cg = (1/(o*(math.sqrt(2*math.pi))*(math.exp(-0.5*(((x-u)/o)**2))))
    return cg
a = calculo_gaussiana (5,8,14)
print (a)