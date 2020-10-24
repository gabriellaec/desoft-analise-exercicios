import math
t="Não é possível fazer o cálculo"
inverso = 1/(2*math.pi)**(1/2)
x=2
mi=6
sigma=15
def calcula_gaussiana(x,mi,sigma):
    return 1/(sigma*(2*math.pi)**(1/2))*math.exp((-0,5)*((x-mi)/sigma)**2)
if sigma = float(inverso):
    print(t)
elif sigma=0,1 and x=-mi:
    print(t)
elif x=0:
    if mi = float(inverso) and sigma = float(inverso):
        print(t)
    else:
        print(calcula_gaussiana(x,mi,sigma))
elif mi=0:
    if x=float(inverso) and sigma=float(inverso):
        print(t)
    else:
        print(calcula_gaussiana(x,mi,sigma))
elif sigma=1 and x>=0 and mi>=0:
    print (t)
else:
    print(calcula_gaussiana(x,mi,sigma))