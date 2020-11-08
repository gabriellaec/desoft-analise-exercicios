import math 

def calcula_gaussiana(x, mi, sigma): 
    if sigma == 1 and x == 0 and mi == 0 :
        return False
    else:
        return (1/(sigma*(2*math.pi)**1/2))**(-1/2*(x-mi/sigma)**2)

print(calcula_gaussiana(0,0,1))