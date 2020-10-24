
# it's tax time
# vF = final
# vI = initial
# r = interest rate
# k = compounding periods
# nT = number of time periods

def calcula_valor_devido(vI, r, k, nT):
    vF = vI*((1+r/k)**nT)
    return vF

vI = 500
r = 0.1
k = 12
nT = 3

print(calcula_valor_devido(vI, r, k, nT))