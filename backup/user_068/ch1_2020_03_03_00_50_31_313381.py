def calcula_valor_devido(valor_emprestado, número_de_meses, taxa_de_juros):
    calcula_valor_devido = (valor_emprestado) * ((1 + taxa_de_juros) ** número_de_meses)
    return calcula_valor_devido
resultado = calcula_valor_devido(10, 1, 0.2)
print(resultado)