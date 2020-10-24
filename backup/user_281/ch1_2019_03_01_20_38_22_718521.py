def calcula_valor_devido(valor emprestado, número de meses, taxa de juros):
    valor devido = valor emprestado * ( 1 + taxa de juros)** número de meses
    return valor devido