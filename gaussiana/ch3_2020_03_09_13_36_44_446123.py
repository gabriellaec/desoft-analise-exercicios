import math
sigma = 2
x =4
mi =2

var1 =1/(sigma * math.sqrt (2*math.pi))
var2 = (x - mi)/sigma

def gauss (x,y):
    z= x*math.e**(-0.5*y**2)
    return z
funcao =gauss (var1,var2)
print (funcao)
