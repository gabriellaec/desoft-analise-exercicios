def calcula_valor_devido(C,t,J):
    M = C*((1+J)**t)
    return M

Divida = calcula_valor_devido(100,2,0.5)
print(Divida)