def calcula_valor_devido
    y=int(valor_emprestado)*(1+int(taxa_de_juros))**int(numero_de_meses)
    return y
