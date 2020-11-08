#math nerd time
#receive 3 real numbers - a, b, c
#return formula:
#f(a, b, c) = (1/(c*sqrt(2*pi)))*math.e**(-0.5*((a-b)/c)**2)

from math import e
from math import pi

def calcula_gaussiana(a,b,c):
    f= (1/(c*(2*pi)**1/2))*e**(-0.5*((a-b)/c)**2)
    return f

a=50
b=80
c=594

if (a == 0 and b == 0 and c == 1):
    print(calcula_gaussiana(a,b,c))
elif (a > 0 and b > 0 and c == 1):
    print(calcula_gaussiana(a,b,c))
elif (c == (2*pi)**2):
    print(calcula_gaussiana(a,b,c))
elif(a == 0 and b == (2*pi)**2 and c == (2*pi)**2):
    print(calcula_gaussiana(a,b,c))
elif(b == 0 and a == (2*pi)**2 and c == (2*pi)**2):
    print(calcula_gaussiana(a,b,c))
else:
    print(calcula_gaussiana(a,b,c))
