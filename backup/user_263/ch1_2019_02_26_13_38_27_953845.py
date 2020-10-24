def calcula_valor_devido(valor_emprestado,número_meses,taxa_juros):
    devido=valor_emprestado*(1+taxa_juros)**número_meses
    return devido
