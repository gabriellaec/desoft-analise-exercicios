def calcula_valor_devido(valor_emprestado, numero_de_meses, taxa_de_juros):
    if numero_de_meses != 0:
        valor_devido = valor_emprestado * numero_de_meses**taxa_de_juros
    else:
        valor_devido = valor_emprestado
    return valor_devido