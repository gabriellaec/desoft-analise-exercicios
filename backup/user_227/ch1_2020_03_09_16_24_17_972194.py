def calcula_valor_devido(valor_emprestado, taxa_de_juros, numero_de_meses):
    y = valor_emprestado*(1+taxa_de_juros)**numero_de_meses
    return y
    