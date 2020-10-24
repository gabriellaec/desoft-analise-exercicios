def calcula_valor_devido
    valor_devido=int(valor_emprestado)*(1+int(taxa_de_juros))**int(numero_de_meses)
    return valor_devido
