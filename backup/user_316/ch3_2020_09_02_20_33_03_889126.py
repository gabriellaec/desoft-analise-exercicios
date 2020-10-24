import math

def calcula_gaussiana(x, mi, sigma):
    neg_hf = -0.5
    exp = neg_hf*((x-mi)/sigma)**2
    pw = 10 ** exp
    return ( 1/(sigma*math.sqrt(2*math.pi)) )*pw


print(calcula_gaussiana(1, 2, 3))
print(calcula_gaussiana(0, 0, 1))
print(calcula_gaussiana(0, 1/math.sqrt(2*math.pi), 1/math.sqrt(2*math.pi)))
print(calcula_gaussiana(1/math.sqrt(2*math.pi), 0, 1/math.sqrt(2*math.pi)))