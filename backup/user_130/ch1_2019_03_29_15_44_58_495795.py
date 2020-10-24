def calcula_valor_devido(Valor_emprestado,numero_de_meseses,taxa_de_juros):
    y=Valor_emprestado*((1+taxa_de_juros)**numero_de_meses)
    return y