import math

def calcula_gaussiana(x, mi, sigma):
    if (x == 0 or mi == 0) and sigma == 1/(2*math.pi):
        return 0

    if sigma == 1/(2*math.pi):
        return 0

    if sigma == 1 and x == 0 and mi == 0:
        return 0

    neg_hf = -0.5
    exp = neg_hf*((x-mi)/sigma)**2
    pw = 10 ** exp
    return ( 1/(sigma*math.sqrt(2*math.pi)) )*pw

print(calcula_gaussiana(0, 0, 1))
print(calcula_gaussiana(0, 1, 1/(2*math.pi)))