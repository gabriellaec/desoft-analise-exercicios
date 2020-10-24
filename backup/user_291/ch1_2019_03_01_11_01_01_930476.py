def calcula_valor_devido(valor_emprestado, meses, juros):
    y = valor_emprestado*(1 + juros)**meses
    return y
