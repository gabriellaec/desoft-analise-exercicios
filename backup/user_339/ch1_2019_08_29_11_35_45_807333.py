def calcula_valor_devido(ve,n,j):
    # ve = valor emprestado
    # n = número de meses
    # j = taxa de juros
    
    vf = ve * (1 + j / 100) ** n
    return vf
