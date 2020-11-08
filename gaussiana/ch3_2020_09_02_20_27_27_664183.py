import math

def calcula_gaussiana(x, mi, sigma):
    if x == 0 or mi == 0 or sigma == 1/(2*math.pi):
        return 0

    neg_hf = -0.5
    exp = neg_hf*((x-mi)/sigma)**2
    pw = 10 ** exp
    return ( 1/(sigma*math.sqrt(2*math.pi)) )*pw

print(calcula_gaussiana(1, 2, 3))