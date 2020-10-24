def calcula_valor_devido(valor emprestado, número de meses , taxa de juros):
    calcula_valor_devido=valor emprestado*[(1-taxa de juros)**número de meses-1]
    return calcula_valor_devido