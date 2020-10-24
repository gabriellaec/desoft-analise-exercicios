def calcula_valor_devido(ve,n,j):
    # ve = valor emprestado
    # n = número de meses
    # j = taxa de juros
    
    vf = ve * (1 + j / 100) ** (n/12)
    return vf

x = calcula_valor_devido(500,12,10)

print('{:.2f}'.format(x))