
# it's tax time
# vF = final
# vI = initial
# r = interest rate
# k = compounding periods
    #k removed for overkill?
# nT = number of time periods

def calcula_valor_devido(vI, r, nT):
    vF = vI*((1+r)**nT)
    return vF

vI = 500
r = 0.1
nT = 3

if (vI == 0 and r != 0 and nT != 0):
    print('Valor de empréstimo inicial igual a zero.')
    print(calcula_valor_devido(vI, r, nT))
elif (vI != 0 and r == 0 and nT != 0):
    print('Juros igual a zero. Não há cálculo a ser feito.')
elif (vI != 0 and r != 0 and nT == 0):
    print(calcula_valor_devido(vI, r, nT))
elif(vI == 0 and r == 0 and nT == 0):
    print('Todos os valores iguais a zero. Não há cálculo a ser feito.')
else:
    print(calcula_valor_devido(vI, r, nT))
