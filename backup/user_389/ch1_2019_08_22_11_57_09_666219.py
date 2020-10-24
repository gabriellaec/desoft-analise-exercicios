def calcula_valor_devido(vf, j, n):
    pu=vf/(1+j/100)**(n/252)
    return pu

x = calcula_valor_devido(1000, 5.99, 599)
print(x)

