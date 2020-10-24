def calcula_valor_devido(valor_emprestado, numero_de_meses, taxa_de_juros):
    r = valor_emprestado * (1 + taxa_de_juros)**numero_de_meses
    return r