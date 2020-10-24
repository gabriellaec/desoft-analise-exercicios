def calcula_valor_devido(C,J,t):
    M = C*((1+J)**t)
    return M

Divida = calcula_valor_devido(100,0.5,2)
print(Divida)