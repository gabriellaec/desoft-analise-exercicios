def calcula_valor_devido(valor_emprestado,taxa_de_juros,número_de_meses):
    valor_devido=(valor_emprestado)*((1+taxa_de_juros)**número_de_meses)
    return valor_devido