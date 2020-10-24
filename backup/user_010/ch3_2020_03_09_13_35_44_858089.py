import math
sigma = float(input("Sigma: "))
x =float(input("X: "))
mi =float(input("Mi: "))

var1 =1/(sigma * math.sqrt (2*math.pi))
var2 = (x - mi)/sigma

def gauss (x,y):
    z= x*math.e**(-0.5*y**2)
    return z
funcao =gauss (var1,var2)
print (funcao)
