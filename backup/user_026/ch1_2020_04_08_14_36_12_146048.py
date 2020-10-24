def calcula_valor_devido(valor_emprestado, num_meses, taxa_juros): 
    valor_devido = valor_emprestado*(1+taxa_juros)**num_meses
    return valor_devido