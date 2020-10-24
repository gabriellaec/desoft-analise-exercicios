def calcula_valor_devido(valor_emprestado, meses, taxas_juros):
    y = valor_emprestado  * (1 + taxas_juros) ** meses
    return y

valor_emprestado = 1000
meses = 7
taxas_juros = 0.3