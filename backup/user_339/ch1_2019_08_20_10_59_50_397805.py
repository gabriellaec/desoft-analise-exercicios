def calcula_valor_devido(ve,m,j):
    # ve = valor emprestado
    # n = número de meses
    # j = taxa de juros
    
    vf = ve * (1 + j / 100) ** n
    return vf

x = calcula_valor_devido(500,12,10)

print('{:.2f}'.format(x))