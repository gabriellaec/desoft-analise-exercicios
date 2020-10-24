def calcula_valor_devido(val_emprestado, num_meses, taxa_juros):
    y=val_emprestado*((1+taxa_juros)**num_meses)
    return y
