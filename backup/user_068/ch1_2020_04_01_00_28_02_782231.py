def calcula_valor_devido(valor_emprestado, número_de_meses, taxa_de_juros):
    a = (valor_emprestado) * ((1 + taxa_de_juros) ** número_de_meses)
    return a
resultado = calcula_valor_devido(10, 1, 0.2)
print(resultado)