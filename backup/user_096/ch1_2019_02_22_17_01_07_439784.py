def calcula_valor_devido(valor_emprestado, n_de_meses, taxa_de_juros):
    valor_devido = valor_emprestado*(1+taxa_de_juros)**n_de_meses
    return valor_devido
