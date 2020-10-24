def calcula_valor_devido(C,t,i):
    F =  C * (( 1 + i ))**t
    return F
print(calcula_valor_devido(1000,3,10))
