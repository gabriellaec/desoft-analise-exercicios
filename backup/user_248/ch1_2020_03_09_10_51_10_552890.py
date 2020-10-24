def calcula_valor_devido(C,i,n):
    M=C*(1+i/100)**n
    return M
fx=calcula_valor_devido(1000,10,2)
print(fx)