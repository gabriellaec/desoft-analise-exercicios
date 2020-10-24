def calcular_valor_devido(valor_emprestado, numero_de_meses, taxa_de_juros):
    valor_devido = valor_emprestado * numero_de_meses**taxa_de_juros
    return valor_devido