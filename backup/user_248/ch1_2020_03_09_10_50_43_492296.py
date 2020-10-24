def calcula_valor_devido(C,i,n):
    M=C*(1+i)**n
    return M
fx=calcula_valor_devido(1000,0.1,2)
print(fx)