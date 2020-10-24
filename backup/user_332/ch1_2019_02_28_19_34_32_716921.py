def calcula_valor_devido(valor_emprestado, n_meses, taxa_juros):
    valor_final = valor_emprestado * (1 + taxa_juros)**n_meses
    return(valor_final)