def calcula_valor_devido (valor_emprestado, taxa_de_juros, número_de_meses):
    x = valor_emprestado * (1 + taxa_de_juros)**número_de_meses
    return x