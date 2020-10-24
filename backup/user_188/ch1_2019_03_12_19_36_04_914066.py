def calcula_valor_devido(valor_emprestado, meses, taxa_juros):
    juros = valor_emprestado * (( 1 + taxa_juros ) ** meses)
    return juros