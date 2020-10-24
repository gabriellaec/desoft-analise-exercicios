def calcula_valor_devido(valor emprestado,taxa de juros,número de meses):
    m = valor emprestado * (1+taxa de juros)**número de meses
    return m
print (calcula_valor_devido(1000,2,5))